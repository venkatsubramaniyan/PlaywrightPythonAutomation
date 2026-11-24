
import logging

from playwright.sync_api import Page, expect
from config.settings import BASE_URL

logger = logging.getLogger(__name__)


def test_opencart_homepage_loads(page: Page):
    logger.info("Opening OpenCart homepage")

    page.goto(BASE_URL)

    expect(page).to_have_title("Your Store")

    logger.info("Homepage loaded successfully")
