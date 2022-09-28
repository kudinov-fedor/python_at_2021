from selenium.webdriver.common.by import By

FULL_NAME_INPUT = By.ID, "userName"
EMAIL_INPUT = By.ID, "userEmail"
CURRENT_ADDRESS_TEXTAREA = By.XPATH, "//textarea[@id='currentAddress']"
PERMANENT_ADDRESS_TEXTAREA = By.XPATH, "//textarea[@id='permanentAddress']"
SUBMIT_BUTTON = By.ID, "submit"
NAME_TEXT = By.ID, "name"
EMAIL_TEXT = By.ID, "email"
CURRENT_ADDRESS_TEXT = By.XPATH, "//p[@id='currentAddress']"
PERMANENT_ADDRESS_TEXT = By.XPATH, "//p[@id='permanentAddress']"
