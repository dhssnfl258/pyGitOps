import json
from github import Github
from utils.token_utils import is_github_token_valid
from utils import github_manage
from utils.github_manage.invite import add_repo_member

'''
Repository  module
리포지토리 생성, 삭제, 목록 출력
'''
# print repository list
def list_repositories(org):
    print("\nRepositories:")
    for repo in org.get_repos():
        print(f" - {repo.name}")

# Create GitHub repository ::: default private repository
def create_repository(repo_name, org):
    try:
        repo = org.create_repo(repo_name, private=True)
        print(f"\nRepository created: {repo.html_url}")
        #add users
        add_repo_member(org, repo_name)
    except Exception as e:
        print(f"\nFailed to insert repository: {e}")

# Delete repository
def delete_repository(repo_name, org):
    try:
        repo = org.get_repo(repo_name)
        repo.delete()
        print(f"\nRepository deleted: {repo_name}")
    except Exception as e:
        print(f"\nFailed to delete repository: {e}")

# Repository information
def repository_info(org, reoisitory):
    myrepo = Github.get_repo(reoisitory)
    repo = org.get_repo(myrepo)
    print(repo.name)
    
