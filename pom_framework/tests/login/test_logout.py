from playwright.sync_api import Page, expect

from pom_framework.src.pages.LoginPage import LoginPage
from pom_framework.src.pages.ProductListPage import ProductListPage


def test_logout(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    login_page = LoginPage(page)
    login_page.do_login(credentials)
    products_page = ProductListPage(page)
    products_page.click_logout()
    expect(login_page._login_btn).to_be_visible()
