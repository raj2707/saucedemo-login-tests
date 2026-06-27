# Saucedemo Login Tests

![Playwright Tests](https://github.com/raj2707/saucedemo-login-tests/actions/workflows/playwright.yml/badge.svg)

Automated login tests for saucedemo.com using Playwright + pytest,
structured with Page Object Model (POM).

## Tech stack
- Python 3.12
- Playwright (sync API)
- pytest + pytest-html
- GitHub Actions CI/CD (chromium, firefox, webkit)

## Test scenarios
- Valid login (3 user types)
- Locked-out user error
- Wrong password error
- Empty username / password / both fields

## How to run
pip install -r requirements.txt
playwright install chromium
pytest tests/ -v

## CI/CD
Tests run automatically on every push via GitHub Actions across 3 browsers in parallel.