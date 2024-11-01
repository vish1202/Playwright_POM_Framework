class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._product_header = page.locator(".title")
        self._burger_menu = page.locator("#react-burger-menu-btn")
        self._logout_btn = page.locator("#logout_sidebar_link")

    def click_burger_menu(self):
        self._burger_menu.click()

    def click_logout(self):
        self.click_burger_menu()
        self._logout_btn.click()