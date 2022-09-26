from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_FIELD = (By.CSS_SELECTOR, "#userName")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    SUBMIT_BUTTON = (By.ID, "login")


class BooksPageLocators:
    NON_EMPTY_ROW = (By.XPATH, '//div[@class="rt-table"]//img/ancestor::div[@role="rowgroup"]')
