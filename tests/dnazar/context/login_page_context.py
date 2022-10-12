from selenium.webdriver.remote.webdriver import WebDriver
from tests.dnazar import context
from tests.dnazar.context.common_book_store_context import CommonBookStoreContext
from tests.dnazar.pom.login_page_elements import LoginPageElements


class LoginPageContext(CommonBookStoreContext):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.elements = LoginPageElements(self.driver)

    def fill_user_name_field(self, value: str):
        return self.fill_field(self.elements.get_user_name_input(), value)

    def fill_password_field(self, value: str):
        return self.fill_field(self.elements.get_password_input(), value)

    def click_login_button(self):
        self.click_button(self.elements.get_login_button())
        return context.ProfilePageContext(self.driver).on_load()
