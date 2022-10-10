from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from tests.msonta.books_app.locators import *


class BasePage(BasePageLocators):
    host = "https://demoqa.com"
    url = ""
    timeout = 5

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        return self.driver.get(self.host + self.url)

    def navigate_to_page(self, locator):
        self.scroll_down()
        self.get_element(*locator).click()
        self.driver.implicitly_wait(2)
        return self

    def get_element(self, by, value):
        return self.driver.find_element(by, value)

    def get_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def scroll_down(self):
        return self.driver.execute_script("window.scrollTo(0, 500);")

    def scroll_up(self):
        return self.driver.execute_script("window.scrollTo(0, 0);")

    def get_books_count(self, locator):
        books = self.get_elements(*locator)
        return len(books)

    def get_alert(self):
        WebDriverWait(self.driver, self.timeout) \
            .until(ec.alert_is_present())

        return self.driver.switch_to.alert

    def accept_alert(self, alert):
        alert.accept()
        self.driver.implicitly_wait(2)
        return self

    def accept_modal(self):
        self.get_element(*self.ACCEPT_MODAL_BUTTON).click()
        return self

    def get_books(self):
        return self.get_elements(*self.BOOKS)


class LoginPage(BasePage, LoginPageLocators):
    url = "/login"

    def login(self, user_name, password):
        self.get_element(*self.USER_FIELD).send_keys(user_name)
        self.get_element(*self.PASSWORD_FIELD).send_keys(password)
        self.get_element(*self.SUBMIT_BUTTON).click()

        WebDriverWait(self.driver, self.timeout) \
            .until(ec.presence_of_element_located(self.BOOKS_TABLE))
        return self

    def logout(self):
        self.get_element(*self.LOGOUT_BUTTON).click()


class BookPage(BasePage, BooksPageLocators):
    url = "/books"

    def search(self, value):
        search_box = self.get_element(*self.SEARCH_INPUT)
        search_box.send_keys(value)

    def get_book_item_link(self, book_title):
        return self.get_element(By.XPATH, f"//a[text()='{book_title}']")

    def add_book_to_collection(self, book_title):
        self.get_book_item_link(book_title).click()
        self.scroll_down()
        self.get_element(*self.ADD_TO_COLLECTION_BUTTON).click()


class ProfilePage(BasePage, ProfilePageLocators):
    url = "/profile"

    def delete_book(self, book_name):
        self.get_element(By.XPATH, f"//div[@class='rt-td' and contains(.,'{book_name}')]/following-sibling::div"
                                   f"//span[@id='delete-record-undefined'] ").click()
        self.accept_modal()

    def delete_all_books(self):
        self.get_element(*self.DELETE_ALL_BOOKS).click()
        self.accept_modal()
