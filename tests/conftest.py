
import pytest
from playwright.sync_api import Playwright

from api.api_client import APIClient
from config.settings import API_BASE_URL


@pytest.fixture
def api_client(playwright: Playwright):
    request_context = playwright.request.new_context(
        base_url=API_BASE_URL,
        extra_http_headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )

    yield APIClient(request_context)

    request_context.dispose()
