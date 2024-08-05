# import json
# from utils.token_utils import is_github_token_valid
# from utils import github_manage
# from github import Github
# import requests
    
# def list_repositories(org):
#     print("\nRepositories:")
#     for repo in org.get_repos():
#         print(f" - {repo.name}")

# # 새로운 리포지토리 생성
# def create_repository(repo_name, org):
#     repo = org.create_repo(repo_name, private=True)
#     repo_permissions = {
#         1: 'pull',  # 읽기 권한
#         2: 'push',  # 쓰기 권한
#         3: 'admin'  # 관리자 권한
#     }
#     while True:
#         repo_member = input("\nAdd Repository Member (or 'N' to finish): ")
#         if repo_member.upper() == 'N':
#             break
#         print("##### SELECT PERMISSION #####")
#         print("1. pull")
#         print("2. push")
#         print("3. admin")
#         try:
#             permission_number = int(input("\nSelect permission: "))
#             if permission_number not in repo_permissions:
#                 print("Invalid permission number. Please try again.")
#                 continue
#             permission = repo_permissions[permission_number]
#             # user = org.get_member(repo_member)
#             repo.add_to_collaborators(repo_member, permission)
#             print(f"User {repo_member} added to repository {repo_name} with {permission} permission.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#         except Exception as e:
#             print(f"Failed to add user {repo_member}: {e}")
        
#     print(f"\nRepository created: {repo.html_url}")

# # 리포지토리 삭제
# def delete_repository(repo_name, org):
#     try:
#         repo = org.get_repo(repo_name)
#         repo.delete()
#         print(f"\nRepository deleted: {repo_name}")
#     except Exception as e:
#         print(f"\nFailed to delete repository: {e}")

# # 메뉴 출력 및 선택 처리
# def print_menu():
#     print("\nMenu:")
#     print("1. Create Repository")
#     print("2. Delete Repository")
#     print("3. Invite Member")
#     print("4. Remove Member")
#     print("5. List Members")
#     print("0. Exit")

# if __name__ == '__main__':
#     main()