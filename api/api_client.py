
from playwright.sync_api import APIRequestContext, APIResponse


class APIClient:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def get(self, endpoint: str, **kwargs) -> APIResponse:
        return self.request.get(endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> APIResponse:
        return self.request.post(endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> APIResponse:
        return self.request.put(endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> APIResponse:
        return self.request.delete(endpoint, **kwargs)
