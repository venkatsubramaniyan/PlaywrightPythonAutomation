
from playwright.sync_api import Page
from locators import account_success_locators


class AccountSuccessPage:
    def __init__(self, page: Page):
        self.page = page

    def get_account_created_message(self) -> str:
        return self.page.get_by_role(
            "heading",
            name=account_success_locators.ACCOUNT_CREATED_HEADING
        ).inner_text()

    def continue_to_account(self) -> None:
        self.page.get_by_role(
            "link",
            name=account_success_locators.CONTINUE_LINK
        ).click()

        self.page.wait_for_url(
            "**/index.php?route=account/account"
        )
