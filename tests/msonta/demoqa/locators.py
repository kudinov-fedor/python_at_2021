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


class ButtonPageLocators(object):
    double_click_button = (By.ID, "doubleClickBtn")
    right_click_button = (By.ID, "rightClickBtn")
    click_me_button = (By.XPATH, "//*[ text()= 'Click Me']")
    double_click_msg = (By.ID, "doubleClickMessage")
    right_click_msg = (By.ID, "rightClickMessage")
    click_me_msg = (By.ID, "dynamicClickMessage")
    ads = (By.TAG_NAME, "iframe")
