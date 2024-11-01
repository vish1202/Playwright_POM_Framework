from playwright.sync_api import expect

from pom_framework.src.pages.CartPage import CartPage
from pom_framework.src.pages.CheckoutPage import CheckoutPage
from pom_framework.src.pages.LoginPage import LoginPage
from pom_framework.src.pages.ProductListPage import ProductListPage


def test_place_order(set_up_tear_down) -> None:
    page = set_up_tear_down
    login_page = LoginPage(page)
    products_page = ProductListPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    login_page.do_login(credentials)
    header = products_page._product_header
    expect(header).to_have_text("Products")
    cart_page.click_add_to_cart_or_remove("Sauce Labs Bike Light")
    cart_page.click_add_to_cart_or_remove("Sauce Labs Backpack")
    cart_page._cart_icon.click()
    cart_page.click_checkout_btn()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout_page.enter_firstname("Vishal")
    checkout_page.enter_lastname("Dewani")
    checkout_page.enter_postal_code("580056")
    checkout_page._continue_btn.click()
    checkout_page._finish_btn.click()
    expect(checkout_page._order_success_msg).to_have_text("Thank you for your order!")
