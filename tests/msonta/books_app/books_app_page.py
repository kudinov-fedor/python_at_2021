from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    host = "https://demoqa.com"
    url = ""
    timeout = 5
    login_button_locator = (By.ID, "login")
    books_table_locator = (By.CSS_SELECTOR, "div.ReactTable")
    modal_locator = (By.CSS_SELECTOR, "div.modal-content")
    accept_modal_button_locator = (By.XPATH, "//*[@id='closeSmallModal-ok']")
    books_locators = (By.XPATH, "//div[contains(@class, 'books-wrapper')]"
                                "//img/ancestor::div[contains(@class, 'rt-tr-group')]")

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

    def get_books_count(self, locator):
        books = self.get_elements(*locator)
        return len(books)

    def get_alert(self):
        WebDriverWait(self.driver, self.timeout) \
            .until(EC.alert_is_present())

        return self.driver.switch_to.alert

    def accept_alert(self, alert):
        alert.accept()
        self.driver.implicitly_wait(2)
        return self

    def click_ok_button_modal_window(self):
        self.get_element(*self.accept_modal_button_locator).click()
        return self

    def get_books(self):
        return self.get_elements(*self.books_locators)


class LoginPage(BasePage):
    url = "/login"
    login_button_locator = (By.ID, "login")
    user_name_field_locator = (By.ID, "userName")
    password_field_locator = (By.ID, "password")
    logout_button_locator = (By.ID, "submit")

    def login(self, user_name, password):
        self.get_element(*self.user_name_field_locator).send_keys(user_name)
        self.get_element(*self.password_field_locator).send_keys(password)
        self.get_element(*self.login_button_locator).click()

        WebDriverWait(self.driver, self.timeout) \
            .until(EC.presence_of_element_located(self.books_table_locator))
        return self

    def logout(self):
        self.get_element(*self.logout_button_locator).click()


class BookPage(BasePage):
    url = "/books"
    search_input = (By.ID, "searchBox")
    book_locator = (By.TAG_NAME, "a")
    add_to_collection_locator = (By.CSS_SELECTOR, ".text-right #addNewRecordButton")
    book_store_menu_item = (By.XPATH, "//*[@id='item-2']/span[contains(text(),'Book Store')]")

    def search(self, value):
        search_box = self.get_element(*self.search_input)
        search_box.send_keys(value)

    def get_book_item_link(self, book_title):
        return self.get_element(By.XPATH, f"//a[text()='{book_title}']")

    def add_book_to_collection(self, book_title):
        self.get_book_item_link(book_title).click()
        self.scroll_down()
        self.get_element(*self.add_to_collection_locator).click()


class ProfilePage(BasePage):
    url = "/profile"
    books_locators = (By.XPATH, "//div[contains(@class, 'rt-tbody')]//img/ancestor::div[contains(@class, "
                                "'rt-tr-group')]")
    delete_button_locator = (By.ID, "delete-record-undefined")
    delete_all_button_locator = (By.XPATH, "//*[@id='submit'][contains(text(), 'Delete All Books')]")
    profile_menu_item = (By.XPATH, "//*[@id='item-3']/span[contains(text(),'Profile')]")

    def delete_book(self, book_name):
        self.get_element(By.XPATH, f"//div[@class='rt-td' and contains(.,'{book_name}')]/following-sibling::div"
                                   f"//span[@id='delete-record-undefined'] ").click()
        self.click_ok_button_modal_window()

    def delete_all_books(self):
        self.get_element(*self.delete_all_button_locator).click()
        self.click_ok_button_modal_window()


class SearchBookPage(BasePage):
    pass
