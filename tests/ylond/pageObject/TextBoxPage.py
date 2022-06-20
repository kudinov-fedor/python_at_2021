from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from tests.ylond.pageObject import BasePage


class TextBoxPage(BasePage.BasePage):
    URL = "/text-box"

    label_username = "label#userName-label.form-label"
    label_email = "label#userEmail-label.form-label"
    label_current_address = "label#currentAddress-label.form-label"
    label_permanent_address = "label#permanentAddress-label.form-label"

    textbox_username = "input#userName"
    textbox_email = "input#userEmail.mr-sm-2.form-control"
    textbox_current_address = "textarea#currentAddress.form-control"
    textbox_permanent_address = "textarea#permanentAddress.form-control"

    username_result_field = "//p[@id='name']"
    email_result_field = "//p[@id='email']"
    error_email_result = "input#userEmail.mr-sm-2.field-error.form-control"
    textarea_result_field = "div.border.col-md-12.col-sm-12"

    submit_button = "button#submit"

    def presence_full_name(self) -> str:
        presence_full_name = self.driver.find_element(By.CSS_SELECTOR, self.label_username)
        if presence_full_name is not None:
            return presence_full_name.text
        else:
            print('the element is None!')

    def presence_email(self) -> str:
        presence_email = self.driver.find_element(By.CSS_SELECTOR, self.label_email)
        if presence_email is not None:
            return presence_email.text
        else:
            print('the element is None!')

    def presence_current_address(self) -> str:
        presence_current_address = self.driver.find_element(By.CSS_SELECTOR, self.label_current_address)
        if presence_current_address is not None:
            return presence_current_address.text
        else:
            print('the element is None!')

    def presence_permanent_address(self) -> str:
        presence_permanent_address = self.driver.find_element(By.CSS_SELECTOR, self.label_permanent_address)
        if presence_permanent_address is not None:
            return presence_permanent_address.text
        else:
            print('the element is None!')

    def enter_full_name(self, fullname):
        enter_full_name = self.driver.find_element(By.CSS_SELECTOR, self.textbox_username).send_keys(fullname)
        return self

    def enter_email(self, email):
        enter_email = self.driver.find_element(By.CSS_SELECTOR, self.textbox_email).send_keys(email)
        return self

    def enter_current_address(self, currentAddress):
        enter_current_address = self.driver.find_element(By.CSS_SELECTOR, self.textbox_current_address).send_keys(
            currentAddress)
        return self

    def enter_permanent_address(self, permanentAddress):
        enter_permanent_address = self.driver.find_element(By.CSS_SELECTOR, self.textbox_permanent_address).send_keys(
            permanentAddress)
        return self

    def click_submit_button(self):
        submit_button = self.driver.find_element(By.CSS_SELECTOR, self.submit_button).click()
        return self

    def get_username_text(self) -> str:
        get_username_result = self.driver.find_element(By.XPATH, self.username_result_field)
        if get_username_result is not None:
            return get_username_result.text
        else:
            print('the element is None!')

    def get_error_email_result(self) -> bool:
        get_error_email_result = self.driver.find_element(By.CSS_SELECTOR, self.error_email_result)
        if get_error_email_result is not None:
            return True

    def get_submit_result(self) -> str:
        get_submit_result = self.driver.find_element(By.CSS_SELECTOR, self.textarea_result_field)
        if get_submit_result is not None:
            return get_submit_result.text
        else:
            print('the element is None!')

    def is_element_present(self) -> bool:
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.textarea_result_field)
        except NoSuchElementException:
            return False
        return True
