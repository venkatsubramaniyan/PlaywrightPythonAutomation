
from playwright.sync_api import Page, expect
from config.settings import BASE_URL


def test_opencart_homepage_loads(page: Page):
    page.goto(BASE_URL)

    expect(page).to_have_title("Your Store")
