from playwright.sync_api import Page, expect

from pom_framework.src.pages.LoginPage import LoginPage


def test_login_with_standard_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    login_page.do_login(credentials)
    product_title = page.locator(".title")
    expect(product_title).to_have_text("Products")


def test_login_with_invalid_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce123'}
    login_page = LoginPage(page)
    login_page.do_login(credentials)
    actual_msg = login_page._login_err_msg
    expected_msg = "Epic sadface: Username and password do not match any user in this service"
    expect(actual_msg).to_have_text(expected_msg)


def test_login_with_no_credentials(set_up_tear_down) -> None:
    page = set_up_tear_down
    login_page = LoginPage(page)
    login_page.click_login()
    actual_msg = login_page._login_err_msg
    expected_msg = "Epic sadface: Username is required"
    expect(actual_msg).to_have_text(expected_msg)

