from src.GitHubEndpoints import GitHubEndPoints

class GitHubService:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_user_profile(self):
        endpoint = GitHubEndPoints.USER_PROFILE
        return self.api_client.get(endpoint)

    def list_repositories(self, visibility="all", per_page=50, page=1):
        #endpoint = f"users/{username}/repos"
        endpoint = GitHubEndPoints.REPOSITORIES
        params = {
            "per_page": per_page,
            "page": page,
            "sort": "updated",
            "visibility": visibility
        }
        return self.api_client.get(endpoint, params=params)

    def repository_details(self, repo_name):
        user_profile = self.get_user_profile()
        if not user_profile:
            print("Unable to retrieve user profile; cannot resolve repository owner.")
            return None

        username = user_profile.get('login')
        endpoint = f"repos/{username}/{repo_name}"
        return self.api_client.get(endpoint)