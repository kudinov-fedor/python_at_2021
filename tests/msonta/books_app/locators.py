from selenium.webdriver.common.by import By


class BasePageLocators:
    BOOKS = (By.XPATH, "//div[contains(@class, 'books-wrapper')]//img/ancestor::div[contains(@class, 'rt-tr-group')]")
    BOOKS_TABLE = (By.CSS_SELECTOR, "div.ReactTable")
    ACCEPT_MODAL_BUTTON = (By.XPATH, "//*[@id='closeSmallModal-ok']")


class LoginPageLocators:
    USER_FIELD = (By.CSS_SELECTOR, "#userName")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    SUBMIT_BUTTON = (By.ID, "login")
    LOGOUT_BUTTON = (By.ID, "submit")


class BooksPageLocators:
    SEARCH_INPUT = (By.ID, "searchBox")
    MENU_LINK = (By.XPATH, "//*[@id='item-2']/span[contains(text(),'Book Store')]")
    ADD_TO_COLLECTION_BUTTON = (By.CSS_SELECTOR, ".text-right #addNewRecordButton")
    GO_BACK = (By.CSS_SELECTOR, ".text-left #addNewRecordButton")


class ProfilePageLocators:
    DELETE_ALL_BOOKS = (By.XPATH, "//*[@id='submit'][contains(text(), 'Delete All Books')]")
    MENU_LINK = (By.XPATH, "//*[@id='item-3']/span[contains(text(),'Profile')]")
    BOOKS_TABLE_ITEM = (By.XPATH, "//div[contains(@class, 'rt-tbody')]//img/ancestor::div[contains(@class, "
                                "'rt-tr-group')]")
