from github import Github
import requests


def is_github_token_valid(token):
    """
    Check if the provided GitHub token is valid.

    Args:
    token (str): GitHub token to be checked.

    Returns:
    bool: True if the token is valid, False otherwise.
    """
    # GitHub API endpoint to get the authenticated user's information
    url = "https://api.github.com/user"
    
    # Set the headers with the provided token
    headers = {
        "Authorization": f"token {token}"
    }
    
    # Make the request to the GitHub API
    response = requests.get(url, headers=headers)
    
    # Check the status code
    if response.status_code == 200:
        # Token is valid
        return True
    else:
        # Token is invalid or expired
        return False