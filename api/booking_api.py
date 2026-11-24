
from playwright.sync_api import APIResponse

from api.api_client import APIClient
from constants import api_endpoints


class BookingAPI:
    def __init__(self, client: APIClient):
        self.client = client

    def get_booking_ids(self) -> APIResponse:
        return self.client.get(api_endpoints.BOOKING)

    def get_booking(self, booking_id: int) -> APIResponse:
        return self.client.get(
            api_endpoints.booking_by_id(booking_id)
        )

    def create_booking(self, payload: dict) -> APIResponse:
        return self.client.post(
            api_endpoints.BOOKING,
            data=payload
        )

    def update_booking(
        self, booking_id: int, payload: dict, token: str
    ) -> APIResponse:
        return self.client.put(
            api_endpoints.booking_by_id(booking_id),
            data=payload,
            headers={"Cookie": f"token={token}"}
        )

    def delete_booking(
        self, booking_id: int, token: str
    ) -> APIResponse:
        return self.client.delete(
            api_endpoints.booking_by_id(booking_id),
            headers={"Cookie": f"token={token}"}
        )
