
import os
from dotenv import load_dotenv

load_dotenv()

TEST_ENV = os.getenv("TEST_ENV", "qa").lower()

if TEST_ENV not in ("qa", "uat"):
    raise ValueError(f"Unsupported environment: {TEST_ENV}")

BASE_URL = os.getenv(
    "UI_BASE_URL",
    "https://naveenautomationlabs.com/opencart/"
)

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://restful-booker.herokuapp.com"
)

USERNAME = os.getenv(f"{TEST_ENV.upper()}_USERNAME")
PASSWORD = os.getenv(f"{TEST_ENV.upper()}_PASSWORD")

API_USERNAME = os.getenv("API_USERNAME")
API_PASSWORD = os.getenv("API_PASSWORD")
