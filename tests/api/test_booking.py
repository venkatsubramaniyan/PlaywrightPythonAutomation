
from copy import deepcopy
from http import HTTPStatus

import pytest_check as check

from api.api_client import APIClient
from api.auth_api import AuthAPI
from api.booking_api import BookingAPI
from config.settings import API_USERNAME, API_PASSWORD
from utils.data_factory import generate_booking


def test_get_booking_ids(api_client: APIClient):
    booking_api = BookingAPI(api_client)

    response = booking_api.get_booking_ids()

    check.equal(response.status, HTTPStatus.OK)

    response_body = response.json()

    check.is_instance(response_body, list)
    check.is_true(len(response_body) > 0)


def test_create_booking(api_client: APIClient):
    booking_api = BookingAPI(api_client)

    payload = generate_booking()

    response = booking_api.create_booking(payload)

    check.equal(response.status, HTTPStatus.OK)

    response_body = response.json()

    check.is_in("bookingid", response_body)
    check.equal(response_body.get("booking"), payload)


def test_update_booking(api_client: APIClient):
    booking_api = BookingAPI(api_client)
    auth_api = AuthAPI(api_client)

    # Generate authentication token
    auth_response = auth_api.generate_token(
        API_USERNAME,
        API_PASSWORD
    )

    assert auth_response.status == HTTPStatus.OK

    token = auth_response.json().get("token")
    assert token, "Authentication token was not generated"

    # POST - Create booking
    original_payload = generate_booking()

    create_response = booking_api.create_booking(original_payload)

    assert create_response.status == HTTPStatus.OK

    booking_id = create_response.json().get("bookingid")
    assert booking_id is not None, "Booking ID was not generated"

    # GET - Verify original booking
    original_response = booking_api.get_booking(booking_id)

    check.equal(original_response.status, HTTPStatus.OK)
    check.equal(original_response.json(), original_payload)

    # Prepare updated payload
    updated_payload = deepcopy(original_payload)

    updated_payload["totalprice"] += 100
    updated_payload["depositpaid"] = not original_payload["depositpaid"]

    # PUT - Update booking
    update_response = booking_api.update_booking(
        booking_id,
        updated_payload,
        token
    )

    check.equal(update_response.status, HTTPStatus.OK)
    check.equal(update_response.json(), updated_payload)

    # GET - Verify persisted changes
    updated_response = booking_api.get_booking(booking_id)

    check.equal(updated_response.status, HTTPStatus.OK)
    check.equal(updated_response.json(), updated_payload)
