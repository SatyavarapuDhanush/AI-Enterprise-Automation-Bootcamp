import requests
from urllib.parse import urljoin

class APIClient:
    def __init__(self, base_url, headers=None, timeout=10):
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = timeout

        if headers:
            self.session.headers.update(headers)

    def _request(self, method, endpoint, **kwargs):
        url = urljoin(self.base_url, endpoint)
        kwargs.setdefault('timeout', self.timeout)
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            if response.status_code == 204 or not response.content:
                return response.status_code
            return response.json()
        except requests.Timeout:
            print(f"Request to {url} timed out.")
            return None
        except requests.ConnectionError:
            print(f"Connection error occurred while trying to reach {url}.")
            return None
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
    
    def get(self, endpoint, params=None):
        return self._request('GET', endpoint, params=params)
    
    def post(self, endpoint, data=None):
        return self._request('POST', endpoint, json=data)
    
    def put(self, endpoint, data=None):
        return self._request('PUT', endpoint, json=data)
    
    def delete(self, endpoint):
        return self._request('DELETE', endpoint)





    # def get(self, endpoint, params=None):
    #     url = urljoin(self.base_url, endpoint)
    #     try:
    #         response = self.session.get(url, params=params, timeout=10)
    #         response.raise_for_status()
    #         return response.json()
    #     except requests.timeout:
    #         print(f"Request to {url} timed out.")
    #         return None
    #     except requests.ConnectionError:
    #         print(f"Connection error occurred while trying to reach {url}.")
    #         return None
    #     except requests.HTTPError as http_err:
    #         print(f"HTTP error occurred: {http_err}")
    #         return None

    # def post(self, endpoint, data=None):
    #     url = urljoin(self.base_url, endpoint)
    #     try:
    #         response = self.session.post(url, json=data, timeout=10)
    #         response.raise_for_status()
    #         return response.json()
    #     except requests.timeout:
    #         print(f"Request to {url} timed out.")
    #         return None
    #     except requests.ConnectionError:
    #         print(f"Connection error occurred while trying to reach {url}.")
    #         return None
    #     except requests.HTTPError as http_err:
    #         print(f"HTTP error occurred: {http_err}")
    #         return None
        
    
    # def put(self, endpoint, data=None):
    #     url = urljoin(self.base_url, endpoint)
    #     try:
    #         response = self.session.put(url, json=data, timeout=10)
    #         response.raise_for_status()
    #         return response.json()
    #     except requests.timeout:
    #         print(f"Request to {url} timed out.")
    #         return None
    #     except requests.ConnectionError:
    #         print(f"Connection error occurred while trying to reach {url}.")
    #         return None
    #     except requests.HTTPError as http_err:
    #         print(f"HTTP error occurred: {http_err}")
    #         return None

    # def delete(self,endpoint):
    #     url=urljoin(self.base_url, endpoint)
    #     try:
    #         response = self.session.delete(url, timeout=10)
    #         response.raise_for_status()
    #         return response.status_code
    #     except requests.timeout:
    #         print(f"Request to {url} timed out.")
    #         return None
    #     except requests.ConnectionError:
    #         print(f"Connection error occurred while trying to reach {url}.")
    #         return None
    #     except requests.HTTPError as http_err:
    #         print(f"HTTP error occurred: {http_err}")
    #         return None