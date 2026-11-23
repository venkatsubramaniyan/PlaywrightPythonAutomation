# End-to-end UI test covering login, shopping cart verification, and logout
import pytest_check as check
from playwright.sync_api import Page

from config.settings import BASE_URL, USERNAME, PASSWORD
from constants import expected_messages, products
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.cart_page import CartPage


def test_login_shopping_and_logout(page: Page):
    page.goto(BASE_URL)

    login_page = LoginPage.open_from_home(page)
    login_page.enter_credentials(USERNAME, PASSWORD)

    account_page = login_page.submit_login()
    products_page = account_page.open_phones_category()

    products_page.add_product_to_cart(products.HTC_TOUCH_HD)

    actual_message = products_page.get_add_to_cart_message()
    expected_message = expected_messages.PRODUCT_ADDED_TO_CART.format(
        product_name=products.HTC_TOUCH_HD
    )
    check.equal(actual_message, expected_message)

    products_page.open_tablets_category()
    products_page.add_product_to_cart(products.SAMSUNG_GALAXY_TAB)

    actual_message = products_page.get_add_to_cart_message()
    expected_message = expected_messages.PRODUCT_ADDED_TO_CART.format(
        product_name=products.SAMSUNG_GALAXY_TAB
    )
    check.equal(actual_message, expected_message)

    cart_page = products_page.open_cart()
    account_page = cart_page.proceed_to_checkout()

    for product_name in (
        products.HTC_TOUCH_HD,
        products.SAMSUNG_GALAXY_TAB
    ):
        actual_product = cart_page.get_cart_product_name(product_name)
        check.equal(actual_product, product_name)

    account_page.logout()

    actual_logout_message = account_page.get_logout_message()
    check.equal(
        actual_logout_message,
        expected_messages.ACCOUNT_LOGOUT
    )
