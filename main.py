import json
from github import Github
import os
import sys
from utils.github_manage.repository import list_repositories
from utils.token_utils import is_github_token_valid
from utils.exec import print_menu

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    # Organization Access Token from environment variable
    token = os.getenv('GITHUB_OPS_TOKEN')
    if not token:
        print("Error: GITHUB_OPS_TOKEN environment variable is not set.")
        sys.exit(1)
        
    myGit = Github(token)
    org_name = 'vms-solution-g'
    org = myGit.get_organization(org_name)

    if is_github_token_valid(token):
        print("The GitHub token is valid.")
    else:
        print("The GitHub token is invalid or expired.")
        
    print(f"Organization: {org_name}")
    list_repositories(org)
    print_menu(org)

if __name__ == '__main__':
    main()
