import requests
        
class SourceDataFetcher:
    def __init__(self, urls):
        self.request = requests
        self.urls = urls
    def fetch_data(self, num_requests=None):
        responses = []
        urls_to_fetch = self.urls if num_requests is None else self.urls[:num_requests]
        for url in urls_to_fetch:
            try:
                response = self.request.get(url)
                if response.status_code == 200:
                    responses.append(response)
                else:
                    responses.append(f"Error: Status code {response.status_code} for URL {url}")
            except requests.exceptions.RequestException as e:
                responses.append(f"Request Exception: {e} for URL {url}")
        return responses
