
import pytest
from pages.login_page import LoginPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"

def test_login_valid_user(page):
    login = LoginPage(page)
    login.navigate()
    login.login(VALID_USER, VALID_PASS)
    assert "/inventory.html" in page.url

def test_login_locked_out_user(page):
    login = LoginPage(page)
    login.navigate()
    login.login("locked_out_user", VALID_PASS)
    assert "Sorry, this user has been locked out" in login.get_error_message()

def test_login_wrong_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login(VALID_USER, "parola_gresita")
    assert "Username and password do not match" in login.get_error_message()

def test_login_empty_username(page):
    login = LoginPage(page)
    login.navigate()
    login.login("", VALID_PASS)
    assert "Username is required" in login.get_error_message()

def test_login_empty_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login(VALID_USER, "")
    assert "Password is required" in login.get_error_message()

def test_login_empty_both_fields(page):
    login = LoginPage(page)
    login.navigate()
    login.login("", "")
    assert "Username is required" in login.get_error_message()

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
])
def test_login_multiple_valid_users(page, username, password):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)
    assert "/inventory.html" in page.url