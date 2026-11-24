
import logging

import pytest_check as check
from playwright.sync_api import Page

from config.settings import BASE_URL, USERNAME, PASSWORD
from constants import expected_messages, products
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_login_shopping_and_logout(page: Page):
    logger.info("Starting shopping workflow")

    page.goto(BASE_URL)

    login_page = LoginPage.open_from_home(page)
    login_page.enter_credentials(USERNAME, PASSWORD)

    account_page = login_page.submit_login()
    logger.info("Login completed")

    products_page = account_page.open_phones_category()

    logger.info("Adding product: %s", products.HTC_TOUCH_HD)
    products_page.add_product_to_cart(products.HTC_TOUCH_HD)

    actual_message = products_page.get_add_to_cart_message()
    expected_message = expected_messages.PRODUCT_ADDED_TO_CART.format(
        product_name=products.HTC_TOUCH_HD
    )

    logger.info("Product notification: %s", actual_message)
    check.equal(actual_message, expected_message)

    products_page.open_tablets_category()

    logger.info("Adding product: %s", products.SAMSUNG_GALAXY_TAB)
    products_page.add_product_to_cart(products.SAMSUNG_GALAXY_TAB)

    actual_message = products_page.get_add_to_cart_message()
    expected_message = expected_messages.PRODUCT_ADDED_TO_CART.format(
        product_name=products.SAMSUNG_GALAXY_TAB
    )

    logger.info("Product notification: %s", actual_message)
    check.equal(actual_message, expected_message)

    cart_page = products_page.open_cart()
    account_page = cart_page.proceed_to_checkout()

    logger.info("Verifying shopping cart contents")

    for product_name in (
        products.HTC_TOUCH_HD,
        products.SAMSUNG_GALAXY_TAB
    ):
        actual_product = cart_page.get_cart_product_name(product_name)

        logger.info("Product found in cart: %s", actual_product)
        check.equal(actual_product, product_name)

    logger.info("Logging out")
    account_page.logout()

    actual_logout_message = account_page.get_logout_message()

    logger.info("Logout response: %s", actual_logout_message)
    check.equal(
        actual_logout_message,
        expected_messages.ACCOUNT_LOGOUT
    )
