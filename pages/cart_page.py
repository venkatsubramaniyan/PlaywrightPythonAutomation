
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from playwright.sync_api import Page
from locators import cart_locators

if TYPE_CHECKING:
    from pages.account_page import AccountPage


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def open_cart_dropdown(self) -> None:
        self.page.get_by_role(
            "button",
            name=re.compile(re.escape(cart_locators.CART_SUMMARY))
        ).click()

    def get_cart_product_name(self, product_name: str) -> str:
        return self.page.locator(
            "#content"
        ).get_by_text(
            product_name,
            exact=True
        ).inner_text()

    def proceed_to_checkout(self) -> AccountPage:
        from pages.account_page import AccountPage

        self.page.locator("#cart").get_by_role(
            "link",
            name=cart_locators.CHECKOUT
        ).click()

        self.page.wait_for_url(
            "**/index.php?route=checkout/cart"
        )

        return AccountPage(self.page)
