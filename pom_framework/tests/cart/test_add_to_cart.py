from playwright.sync_api import expect

from pom_framework.src.pages.CartPage import CartPage
from pom_framework.src.pages.LoginPage import LoginPage
from pom_framework.src.pages.ProductListPage import ProductListPage


def test_add_to_cart(set_up_tear_down) -> None:
    page = set_up_tear_down
    login_page = LoginPage(page)
    products_page = ProductListPage(page)
    cart_page = CartPage(page)

    credentials = {"username": "standard_user", "password": "secret_sauce"}
    login_page.do_login(credentials)
    header = products_page._product_header
    expect(header).to_have_text("Products")
    cart_page.click_add_to_cart_or_remove("Sauce Labs Bike Light")
    cart_page.click_add_to_cart_or_remove("Sauce Labs Backpack")
    cart_count = cart_page._cart_count
    expect(cart_count).to_have_text("2")


def test_remove_product_from_cart(set_up_tear_down) -> None:
    page = set_up_tear_down
    login_page = LoginPage(page)
    # products_page = ProductListPage(page)
    cart_page = CartPage(page)

    credentials = {"username": "standard_user", "password": "secret_sauce"}
    login_page.do_login(credentials)
    cart_page.click_add_to_cart_or_remove("Sauce Labs Bike Light")
    cart_page.click_add_to_cart_or_remove("Sauce Labs Backpack")
    cart_page._cart_icon.click()
    expect(cart_page._cart_count).to_have_text("2")
    cart_page.click_add_to_cart_or_remove("Sauce Labs Bike Light")
    expect(cart_page._cart_count).to_have_text("1")
