from tests.dnazar.pom import login_page_locators as locators
from tests.dnazar.pom.common_book_store_elements import CommonBookStoreElements


class LoginPageElements(CommonBookStoreElements):

    def get_user_name_input(self):
        return self.get_element(locators.USER_NAME_INPUT)

    def get_password_input(self):
        return self.get_element(locators.PASSWORD_INPUT)

    def get_login_button(self):
        return self.get_element(locators.LOGIN_BUTTON)
