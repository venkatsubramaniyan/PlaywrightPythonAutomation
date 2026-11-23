
from playwright.sync_api import Page
from locators import registration_locators
from pages.account_success_page import AccountSuccessPage


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

    def enter_customer_details(self, customer: dict) -> None:
        self.page.get_by_role(
            "textbox",
            name=registration_locators.FIRST_NAME
        ).fill(customer["first_name"])

        self.page.get_by_role(
            "textbox",
            name=registration_locators.LAST_NAME
        ).fill(customer["last_name"])

        self.page.get_by_role(
            "textbox",
            name=registration_locators.EMAIL
        ).fill(customer["email"])

        self.page.get_by_role(
            "textbox",
            name=registration_locators.TELEPHONE
        ).fill(customer["telephone"])

        self.page.get_by_role(
            "textbox",
            name=registration_locators.PASSWORD,
            exact=True
        ).fill(customer["password"])

        self.page.get_by_role(
            "textbox",
            name=registration_locators.CONFIRM_PASSWORD
        ).fill(customer["password"])

    def select_newsletter(self) -> None:
        self.page.get_by_role(
            "radio",
            name=registration_locators.NEWSLETTER_YES
        ).check()

    def accept_privacy_policy(self) -> None:
        self.page.get_by_role(
            registration_locators.PRIVACY_POLICY_ROLE
        ).check()

    def submit_registration(self) -> AccountSuccessPage:
        self.page.get_by_role(
            "button",
            name=registration_locators.CONTINUE_BUTTON
        ).click()

        self.page.wait_for_url(
            "**/index.php?route=account/success"
        )

        return AccountSuccessPage(self.page)
