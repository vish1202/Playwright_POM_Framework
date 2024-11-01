class CartPage:

    def __init__(self, page):
        self.page = page
        self._cart_icon = page.locator("//a[@class='shopping_cart_link']")
        self._cart_count = page.locator("//span[@class='shopping_cart_badge']")
        self._checkout_btn = page.locator("//button[@id='checkout']")

    def get_add_remove_cart_locator(self, product_name):
        return self.page.locator(f"//div[text()='{product_name}']//parent::a//parent::div//following-sibling::div//button")

    def click_add_to_cart_or_remove(self, product_name):
        self.get_add_remove_cart_locator(product_name).click()
        return self

    def click_checkout_btn(self):
        self._checkout_btn.click()