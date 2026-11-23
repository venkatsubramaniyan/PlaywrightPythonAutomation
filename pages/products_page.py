
import re

from playwright.sync_api import Page

from locators import products_locators
from pages.cart_page import CartPage


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def open_phones_category(self) -> None:
        self.page.get_by_role(
            "link",
            name=products_locators.PHONES_CATEGORY
        ).click()

        self.page.wait_for_url(
            "**/index.php?route=product/category*"
        )

    def open_tablets_category(self) -> None:
        self.page.get_by_role(
            "link",
            name=products_locators.TABLETS_CATEGORY
        ).click()

        self.page.wait_for_url(
            "**/index.php?route=product/category*"
        )

    def add_product_to_cart(self, product_name: str) -> None:
        self.page.locator(
            products_locators.add_to_cart_button(product_name)
        ).click()

        self.page.locator(
            products_locators.ADD_TO_CART_SUCCESS_MESSAGE
        ).filter(has_text=product_name).wait_for(state="visible")

    def get_add_to_cart_message(self) -> str:
        message = self.page.locator(
            products_locators.ADD_TO_CART_SUCCESS_MESSAGE
        ).inner_text()

        return re.sub(r"\s+", " ", message).strip().removesuffix("×").strip()

    def open_cart(self) -> CartPage:
        cart_page = CartPage(self.page)
        cart_page.open_cart_dropdown()
        return cart_page
