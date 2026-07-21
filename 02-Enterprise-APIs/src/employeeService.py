

class EmployeeService:
    def __init__(self, api_client):
        self.client = api_client

    def get_all_users(self,params=None):
        return self.client.get("users", params=params)