
from playwright.sync_api import APIResponse

from api.api_client import APIClient
from constants import api_endpoints


class AuthAPI:
    def __init__(self, client: APIClient):
        self.client = client

    def generate_token(
        self, username: str, password: str
    ) -> APIResponse:
        return self.client.post(
            api_endpoints.AUTH,
            data={
                "username": username,
                "password": password,
            }
        )
