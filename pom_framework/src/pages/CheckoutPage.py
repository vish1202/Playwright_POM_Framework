class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self._checkout_btn = page.locator("//button[@id='checkout']")
        self._fname = page.locator("//input[@id='first-name']")
        self._lname = page.locator("//input[@id='last-name']")
        self._zip_code =page.locator("//input[@id='postal-code']")
        self._continue_btn = page.locator("//input[@id='continue']")
        self._finish_btn = page.locator("//button[@id='finish']")
        self._order_success_msg = page.locator("//h2[@class='complete-header']")

    def enter_firstname(self, firstname):
        self._fname.fill(firstname)

    def enter_lastname(self, lastname):
        self._lname.fill(lastname)

    def enter_postal_code(self, zipcode):
        self._zip_code.fill(zipcode)
