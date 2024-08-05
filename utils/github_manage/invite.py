import os
import json
from github import Github
from github.GithubException import GithubException

# Repository member 추가
def add_repo_member(org, repository):
    # permission list
    repo_permissions = {
        1: 'pull',  # 읽기 권한
        2: 'push',  # 쓰기 권한
        3: 'admin'  # 관리자 권한
    }
    try:
        #target repository
        repo = org.get_repo(repository)
        users_file_path = resource_path('data/member.json')
        # users_file_path = os.path.join(os.path.dirname(__file__), '../../data/member.json')
        with open(users_file_path, 'r', encoding='utf-8') as users_file:
            users = json.load(users_file)
        
        print("########## Organization member list ##########")
        # 각 사용자 이름 출력
        for user in users.values():
            print(user)
        
        #add user loop
        while True:
            member_name = input("\nAdd Repository Member (or 'N' to finish): ")
            repo_member = get_key_from_value(users, member_name)
            
            if repo_member == None:
                break
            print("##### SELECT PERMISSION #####")
            print("1: pull")
            print("2: push")
            print("3: admin")
            try:
                permission_number = int(input("\nSelect permission: "))
                if permission_number not in repo_permissions:
                    print("Invalid permission number. Please try again.")
                    continue
                permission = repo_permissions[permission_number]
                # user = org.get_member(repo_member)
                repo.add_to_collaborators(repo_member, permission)
                print(f"User {repo_member} added to repository {repository} with {permission} permission.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"Failed to add user {repo_member}: {e}")
    except GithubException as e:
        return f"Failed to Add {user} to "

# Organization member 초대        
def invite_org_member(org):
    try:
        user = input(f"enter the user id: ")
        actual_name =(f"enter the user's actual name: ") 
        # users.json 파일 업데이트
        users_file_path = os.path.join(os.path.dirname(__file__), '../../users.json')
        with open(users_file_path, 'r', encoding='utf-8') as users_file:
            users = json.load(users_file)
        
        users[user] = actual_name
        
        with open(users_file_path, 'w', encoding='utf-8') as users_file:
            json.dump(users, users_file, ensure_ascii=False, indent=4)
        
        # g = Github(token)
        # org = g.get_organization(org_name)
        # user = g.getuser(user)
        org.add_to_members(user,role="Member")
        return f"Successfully invited {user} to organization!"
    except GithubException as e:
        return f"Failed to print member list to {org}"

# 전체 member 출력
def org_member_list(org):
    try:
        
        users_file_path = os.path.join(os.path.dirname(__file__), '../../data/member.json')
        with open(users_file_path, 'r', encoding='utf-8') as users_file:
            users = json.load(users_file)
                    
        members = org.get_members()
        
        # print(f"Total members in the organization: {len(members)}")
        print("########### All member list ###########")
        i = 1
        for member in members:
            name = users.get(member.login, "Unknown User")
            print(f"{i}. {member.login} [{name}]")
            i += 1
            
            
    except GithubException as e:
        return f"Failed to print member list to {org}"


# def delete_org_member():
# def delete_repo_member():


# def modify_repo_member_permission():




def get_key_from_value(d, value):
    """
    주어진 딕셔너리에서 특정 value에 해당하는 key를 반환합니다.
    
    Args:
    d (dict): 딕셔너리
    value (str): 찾고자 하는 value
    
    Returns:
    str: 해당 value의 key
    """
    for k, v in d.items():
        if v == value:
            return k
    return None