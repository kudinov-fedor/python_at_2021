from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from tests.ylond.pageObject.base_page import BasePage


class TextBoxPage(BasePage):
    URL = "/text-box"

    label_username = By.CSS_SELECTOR, "label#userName-label.form-label"
    label_email = By.CSS_SELECTOR, "label#userEmail-label.form-label"
    label_current_address = By.CSS_SELECTOR, "label#currentAddress-label.form-label"
    label_permanent_address = By.CSS_SELECTOR, "label#permanentAddress-label.form-label"

    textbox_username = By.CSS_SELECTOR, "input#userName"
    textbox_email = By.CSS_SELECTOR, "input#userEmail.mr-sm-2.form-control"
    textbox_current_address = By.CSS_SELECTOR, "textarea#currentAddress.form-control"
    textbox_permanent_address = By.CSS_SELECTOR, "textarea#permanentAddress.form-control"

    username_result_field = By.XPATH, "//p[@id='name']"
    email_result_field = By.XPATH, "//p[@id='email']"
    error_email_result = By.CSS_SELECTOR, "input#userEmail.mr-sm-2.field-error.form-control"
    textarea_result_field = By.CSS_SELECTOR, "div.border.col-md-12.col-sm-12"

    submit_button = By.CSS_SELECTOR, "button#submit"

    def presence_full_name(self) -> str:
        return self.find_element(*self.label_username).text

    def presence_email(self) -> str:
        return self.find_element(*self.label_email).text

    def presence_current_address(self) -> str:
        return self.find_element(*self.label_current_address).text

    def presence_permanent_address(self) -> str:
        return self.find_element(*self.label_permanent_address).text

    def enter_full_name(self, fullname):
        enter_full_name = self.find_element(*self.textbox_username).send_keys(fullname)
        return self

    def enter_email(self, email):
        enter_email = self.find_element(*self.textbox_email).send_keys(email)
        return self

    def enter_current_address(self, currentAddress):
        enter_current_address = self.find_element(*self.textbox_current_address).send_keys(
            currentAddress)
        return self

    def enter_permanent_address(self, permanentAddress):
        enter_permanent_address = self.find_element(*self.textbox_permanent_address).send_keys(
            permanentAddress)
        return self

    def click_submit_button(self):
        submit_button = self.find_element(*self.submit_button).click()
        return self

    def get_username_text(self) -> str:
        if self.find_element(*self.username_result_field) is not None:
            return self.find_element(*self.username_result_field).text
        else:
            print('the element is None!')

    def get_error_email_result(self) -> bool:
        if self.find_element(*self.error_email_result) is not None:
            return True

    def get_submit_result(self) -> str:
        if self.find_element(*self.textarea_result_field) is not None:
            return self.find_element(*self.textarea_result_field).text
        else:
            print('the element is None!')

    def is_element_present(self) -> bool:
        try:
            self.find_element(*self.textarea_result_field)
        except NoSuchElementException:
            return False
        return True

    def fill_form(self, full_name: str = None, email: str = None, current_address: str = None, permanent_address: str = None):
        self.enter_full_name(full_name)
        self.enter_email(email)
        self.enter_current_address(current_address)
        self.enter_permanent_address(permanent_address)
        self.scroll_down()
        self.click_submit_button()
        return self
