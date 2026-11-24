
import logging

import pytest_check as check
from playwright.sync_api import Page

from config.settings import BASE_URL
from constants import expected_messages
from pages.registration_page import RegistrationPage
from utils.data_factory import generate_customer

logger = logging.getLogger(__name__)


def test_customer_registration(page: Page):
    logger.info("Starting customer registration test")

    customer = generate_customer()
    registration_page = RegistrationPage(page)

    page.goto(f"{BASE_URL}index.php?route=account/register")
    logger.info("Opened registration page")

    registration_page.enter_customer_details(customer)
    registration_page.select_newsletter()
    registration_page.accept_privacy_policy()

    logger.info("Submitting customer registration")
    success_page = registration_page.submit_registration()

    actual_message = success_page.get_account_created_message()

    logger.info("Registration response: %s", actual_message)

    check.equal(actual_message, expected_messages.ACCOUNT_CREATED)
