import requests
from urllib.parse import urljoin

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, params=None):
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.timeout:
            print(f"Request to {url} timed out.")
            return None
        except requests.ConnectionError:
            print(f"Connection error occurred while trying to reach {url}.")
            return None
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None

    def post(self, endpoint, data=None):
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.timeout:
            print(f"Request to {url} timed out.")
            return None
        except requests.ConnectionError:
            print(f"Connection error occurred while trying to reach {url}.")
            return None
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        
    
    def put(self, endpoint, data=None):
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.put(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.timeout:
            print(f"Request to {url} timed out.")
            return None
        except requests.ConnectionError:
            print(f"Connection error occurred while trying to reach {url}.")
            return None
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None

    def delete(self,endpoint):
        url=urljoin(self.base_url, endpoint)
        try:
            response = self.session.delete(url, timeout=10)
            response.raise_for_status()
            return response.status_code
        except requests.timeout:
            print(f"Request to {url} timed out.")
            return None
        except requests.ConnectionError:
            print(f"Connection error occurred while trying to reach {url}.")
            return None
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None