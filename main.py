def lambda_handler(event, context):
    github_url = event.get('githubURL')
    
    # Your code logic here
    
    return {
        'statusCode': 200,
        'body': str(github_url)
    }