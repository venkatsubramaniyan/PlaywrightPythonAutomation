
from playwright.sync_api import Page

from locators import account_locators, products_locators
from pages.products_page import ProductsPage


class AccountPage:
    def __init__(self, page: Page):
        self.page = page

    def open_phones_category(self) -> ProductsPage:
        self.page.get_by_role(
            "link",
            name=products_locators.PHONES_CATEGORY
        ).click()

        self.page.wait_for_url(
            "**/index.php?route=product/category*"
        )

        return ProductsPage(self.page)

    def logout(self) -> None:
        self.page.locator(
            account_locators.MY_ACCOUNT
        ).click()

        self.page.get_by_role(
            "link",
            name=account_locators.LOGOUT,
            exact=True
        ).click()

        self.page.wait_for_url(
            "**/index.php?route=account/logout"
        )

    def get_logout_message(self) -> str:
        return self.page.get_by_role(
            "heading",
            name=account_locators.LOGOUT_HEADING
        ).inner_text()
