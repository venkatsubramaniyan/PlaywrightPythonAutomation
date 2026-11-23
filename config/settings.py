
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Select test environment
TEST_ENV = os.getenv("TEST_ENV", "qa").lower()

# Validate environment
if TEST_ENV not in ("qa", "uat"):
    raise ValueError(
        f"Unsupported environment: {TEST_ENV}"
    )

# Application URL
BASE_URL = os.getenv(
    "UI_BASE_URL",
    "https://naveenautomationlabs.com/opencart/"
)

# Environment-specific credentials
USERNAME = os.getenv(f"{TEST_ENV.upper()}_USERNAME")
PASSWORD = os.getenv(f"{TEST_ENV.upper()}_PASSWORD")
