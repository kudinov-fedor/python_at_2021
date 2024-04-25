from tests.khrystynatk.hw5_khr_Page_object.base_page import BasePage


class LoginPage(BasePage):

    def open_login_page(self):
        self.open_page()

    def provide_creds(self):
        self.input_creds(self.USERNAME, self.PASSWORD)
