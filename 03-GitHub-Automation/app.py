import os
from dotenv import load_dotenv  # <--- 1. IMPORT LOAD_DOTENV

# <--- 2. CALL IT BEFORE ANYTHING ELSE RUNS
load_dotenv()

from src.GitHubService import GitHubService
from src.api_client import APIClient


class Main:
    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise ValueError("GITHUB_TOKEN is not set in the environment variables.")
        
        headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github.v3+json",
                "X-GitHub-Api-Version": "2022-11-28"
                }
        
        client = APIClient(
            base_url="https://api.github.com/",
            headers=headers,
            timeout=10
        )

        self.github_service = GitHubService(client)

    def get_user_profile(self):
        return self.github_service.get_user_profile()
    
    def get_all_repositories(self):
        return self.github_service.list_repositories(visibility="all")

    def get_repository_details(self, repo_name):
        return self.github_service.repository_details(repo_name)
    
if __name__ == "__main__":
    main = Main()
    user_profile = main.get_user_profile()
    if user_profile:
        print(f"User Profile: {user_profile.get('login')}, Name: {user_profile.get('name')}")
    
    repositories = main.get_all_repositories()
    if repositories:
        print(f"Total Repositories: {len(repositories)}")
        for repo in repositories:
            print(f"Repository Name: {repo.get('name')}, URL: {repo.get('html_url')}, visibility: {repo.get('visibility')}")
            print("-" * 40)

    repository_details = main.get_repository_details("IndianCulture")
    print(f"Repository Details: {repository_details}")
    if repository_details:
        print(f"Repository Details: {repository_details.get('name')}")
        print(f"Description: {repository_details.get('description')}")
        print(f"Stars: {repository_details.get('stargazers_count')}")
