import requests


def get_repo_files(repo_url):
    # Extract the username and repository name from the URL
    _, _, username, repo_name = repo_url.rstrip('/').split('/')[-4:]
    
    # Construct the API URL to get the repository contents
    api_url = f"https://api.github.com/repos/{username}/{repo_name}/contents"
    
    # Send a GET request to the GitHub API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the file names from the API response
        files = [item['name'] for item in response.json()]
        return files
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

# Example usage
repo_link = "https://github.com/Team-Brewmasters/code-compass-ask-question-lambda"
file_list = get_repo_files(repo_link)
print(file_list)