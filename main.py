import json

from github_api_service import get_repo_file_contents
from open_ai_service import call_chatgpt
from dynamo_cache_service import DynamoCacheService


def lambda_handler(event, context):
    try:
        github_url = event['queryStringParameters']['githubURL']

        _, _, username, repo_name = github_url.rstrip('/').split('/')[-4:]
        print(f"Username: {username}, Repo Name: {repo_name}")

        dynamo_pk = f"{username}/{repo_name}"

        dynamo_cache_service = DynamoCacheService('summary_data')
        summary_data = dynamo_cache_service.get_summary_data(dynamo_pk)

        print(f"Summary Data: {summary_data}")

        if summary_data is not None:
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*',
                    'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
                },
                'body': summary_data
            }
        
        print("Summary data not found in cache. Fetching from GitHub and OpenAI...")

        file_content = get_repo_file_contents(github_url)

        open_ai_response = call_chatgpt(file_content)

        parsed_response = json.loads(open_ai_response)
        repo_name = parsed_response['repository']['name']
        description = parsed_response['repository']['description']
        languages = parsed_response['repository']['technology_stack']['languages']
        frameworks = parsed_response['repository']['technology_stack']['frameworks']
        databases = parsed_response['repository']['technology_stack']['databases']
        tools = parsed_response['repository']['technology_stack']['tools']
        suggested_questions = parsed_response['suggestedQuestions']


        dynamo_cache_service.put_summary_data(dynamo_pk, repo_name, description, languages, frameworks, databases, tools, suggested_questions)
        
        return {
            'statusCode': 200,
            'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*',
                    'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
                },
            'body': json.dumps(open_ai_response)
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': str(e),
            'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET,OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
                },
        }
    
# event = {
#     "githubURL": "https://www.github.com/Team-Brewmasters/code-compass-summary-lambda"
# }

# lambda_handler(event, None)