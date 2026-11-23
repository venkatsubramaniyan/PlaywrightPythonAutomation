
from playwright.sync_api import Page

from locators import login_locators
from pages.account_page import AccountPage


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    @classmethod
    def open_from_home(cls, page: Page) -> "LoginPage":
        page.locator(
            login_locators.MY_ACCOUNT
        ).click()

        page.get_by_role(
            "link",
            name=login_locators.LOGIN_LINK,
            exact=True
        ).click()

        page.wait_for_url(
            "**/index.php?route=account/login"
        )

        return cls(page)

    def enter_credentials(self, username: str, password: str) -> None:
        self.page.get_by_role(
            "textbox",
            name=login_locators.EMAIL
        ).fill(username)

        self.page.get_by_role(
            "textbox",
            name=login_locators.PASSWORD
        ).fill(password)

    def submit_login(self) -> AccountPage:
        self.page.get_by_role(
            "button",
            name=login_locators.LOGIN_BUTTON
        ).click()

        self.page.wait_for_url(
            "**/index.php?route=account/account"
        )

        return AccountPage(self.page)
