import json

from github_api_service import get_repo_file_contents
from open_ai_service import call_chatgpt


def lambda_handler(event, context):
    try:
        github_url = event.get('githubURL')

        file_content = get_repo_file_contents(github_url)

        open_ai_response = call_chatgpt(file_content)
        
        print(open_ai_response)
        return {
            'statusCode': 200,
            'body': json.dumps(open_ai_response)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
    
event = {
    "githubURL": "https://www.github.com/Team-Brewmasters/code-compass-summary-lambda"
}

lambda_handler(event, None)