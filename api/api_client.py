
import logging

from playwright.sync_api import APIRequestContext, APIResponse

logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def get(self, endpoint: str, **kwargs) -> APIResponse:
        logger.info("GET %s", endpoint)
        response = self.request.get(endpoint, **kwargs)
        logger.info("GET %s - Status: %s", endpoint, response.status)
        return response

    def post(self, endpoint: str, **kwargs) -> APIResponse:
        logger.info("POST %s", endpoint)
        response = self.request.post(endpoint, **kwargs)
        logger.info("POST %s - Status: %s", endpoint, response.status)
        return response

    def put(self, endpoint: str, **kwargs) -> APIResponse:
        logger.info("PUT %s", endpoint)
        response = self.request.put(endpoint, **kwargs)
        logger.info("PUT %s - Status: %s", endpoint, response.status)
        return response

    def delete(self, endpoint: str, **kwargs) -> APIResponse:
        logger.info("DELETE %s", endpoint)
        response = self.request.delete(endpoint, **kwargs)
        logger.info("DELETE %s - Status: %s", endpoint, response.status)
        return response
