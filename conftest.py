
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        headless = os.getenv("CI", "false") == "true"
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        yield page
        browser.close()