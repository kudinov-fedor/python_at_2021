from selenium.webdriver.common.by import By


class TextBoxPageLocators(object):
    full_name_input = (By.ID, "userName")
    email_input = (By.ID, "userEmail")
    current_address_input = (By.ID, "currentAddress")
    permanent_address_input = (By.ID, "permanentAddress")
    submit_button = (By.ID, "submit")
    full_name_text = (By.ID, "name")
    email_text = (By.ID, "email")
    current_address_text = (By.CSS_SELECTOR, "p#currentAddress")
    permanent_address_text = (By.CSS_SELECTOR, "p#permanentAddress")
