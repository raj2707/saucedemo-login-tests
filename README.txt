#Login Automation Suite — Saucedemo

Automated login tests for saucedemo.com using Playwright + pytest, structured with Page Object Model (POM).

## Tech stack
- Python 3.11+
- Playwright (sync API)
- pytest

## Test scenarios covered
- Valid login (3 user types)
- Locked-out user error
- Wrong password error
- Empty username / password / both fields

## Project structure
pages/login_page.py   — Page Object (selectors + actions)
tests/test_login.py   — Test cases
conftest.py           — Browser fixtures

