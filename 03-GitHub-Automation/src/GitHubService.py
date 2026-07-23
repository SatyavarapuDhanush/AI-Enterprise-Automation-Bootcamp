

class GitHubService:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_user_profile(self):
        endpoint = "user"
        return self.api_client.get(endpoint)

    def list_repositories(self, visibility="all", per_page=50, page=1):
        #endpoint = f"users/{username}/repos"
        endpoint = "user/repos"
        params = {
            "per_page": per_page,
            "page": page,
            "sort": "updated",
            "visibility": visibility
        }
        return self.api_client.get(endpoint, params=params)