class LoginPage:

    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_btn = page.get_by_text("Login")
        self._login_err_msg = page.locator("h3[data-test='error']")

    def enter_username(self, uname):
        self._username.clear()
        self._username.fill(uname)

    def enter_password(self, pwd):
        self._password.clear()
        self._password.fill(pwd)

    def click_login(self):
        self._login_btn.click()

    def do_login(self, credentials):
        self.enter_username(credentials['username'])
        self.enter_password((credentials['password']))
        self.click_login()
