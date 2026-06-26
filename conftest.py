
import os
import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit"],
        help="Browser to run tests with"
    )


@pytest.fixture(scope="function")
def page(request):
    browser_name = request.config.getoption("--browser")
    headless = os.getenv("CI", "false").lower() == "true"
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=headless)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=headless)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        page = browser.new_page()
        yield page
        page.close()
        browser.close()