import json
from github import Github
import os
from utils.github_manage.repository import list_repositories, delete_repository
from utils.github_manage.invite import add_repo_member, org_member_list, invite_org_member


# 메뉴 출력
def print_menu(org):
    while True:
        print("\nMenu:")    
        print("1. Invite member to ORG")
        print("2. Remove member to ORG")
        print("3. Show members")
        print("4. Repository Management")
        print("0. Exit")
        
        choice = input("\nEnter your choice:::")
        if choice == '1':
            invite_org_member(org)
        elif choice == '2':
            print('test')
        elif choice == '3':
            org_member_list(org)
        elif choice == '4':
            print_repo_menu(org)
        elif choice == '0':
            print("Exiting... Good Bye!")
            break
        else:
            print("Invalid choice. Please try again")

    
    

# repo 메뉴 출력
def print_repo_menu(org):
    while True:
        print("\nRepository Management Menu:")
        print("1. Show all repositories")
        print("2. Create repository")
        print("3. Delete repository")
        print("4. Add members to repository")
        print("5. Delete a member to repository")
        print("6. Modify repository")
        print("0. back to Main")
        
        choice = input("\nEnter your choice:::")
        if choice == '1':
            list_repositories(org)
        elif choice == '2':
            delete_repository(org)
        elif choice == '3':
            add_repo_member(org)
        elif choice == '4':
            print_repo_menu(org)
        elif choice == '5':
            print("choice5")
        elif choice == '0':
            print("Back to main step...")
            break
        else:
            print("Invalid choice. Please try again")