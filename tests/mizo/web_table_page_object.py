from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from collections import namedtuple


class WebPage:
    ROWS = (By.XPATH, "//div[@class='rt-tr-group']")
    ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    SEARCH_BOX = (By.CSS_SELECTOR, "#searchBox")

    def __init__(self, driver):
        self.driver = driver

    def click_button(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def click_add_button(self):
        self.click_button(self.ADD_BUTTON)

    def get_rows(self):
        rows = self.driver.find_elements(*self.ROWS)
        return [ItemRows(row) for row in rows if len(row.text.strip()) != 0]

    def search_by_value(self, locator, value):
        search_field = self.driver.find_element(*locator)
        search_field.send_keys(value)

    def fill_search_field(self, value):
        self.search_by_value(self.SEARCH_BOX, value)

    def create_element(self):
        self.click_add_button()
        return Registration(self.driver)


CellsData = namedtuple("CellsData", ["first_name", "last_name", "email", "age", "salary", "department", "action"])


class ItemRows:
    EDIT_BUTTON = (By.XPATH, ".//span[@class='mr-2']")
    DELETE_BUTTON = (By.XPATH, ".//span[contains(@id, 'delete-record')]")
    CELLS = (By.XPATH, ".//div[@class='rt-td']")

    def __init__(self, element: WebElement):
        self.element = element

    def click_button(self, locator):
        button = self.element.find_element(*locator)
        button.click()

    def click_edit(self):
        self.click_button(self.EDIT_BUTTON)

    def click_delete(self):
        self.click_button(self.DELETE_BUTTON)

    def get_cells(self):
        cells = self.element.find_elements(*self.CELLS)

        cell_data = CellsData(
            *[c.text for c in cells[0:7]]
        )
        return cell_data


class Registration:
    FIELD_LOCATORS = {
        "first_name": (By.CSS_SELECTOR, "#firstName"),
        "last_name": (By.CSS_SELECTOR, "#lastName"),
        "email": (By.CSS_SELECTOR, "#userEmail"),
        "age": (By.CSS_SELECTOR, "#age"),
        "salary": (By.CSS_SELECTOR, "#salary"),
        "department": (By.CSS_SELECTOR, "#department"),
    }
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    def __init__(self, driver):
        self.driver = driver

    def click_button(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def fill_form(self, first_name=None, last_name=None, email=None, age=None, salary=None, department=None):
        field_value_data = locals()
        for field_name, field_value in field_value_data.items():
            if field_name in self.FIELD_LOCATORS and field_value is not None:
                locator = self.FIELD_LOCATORS[field_name]
                field = self.driver.find_element(*locator)
                field.clear()
                field.send_keys(field_value)

    def click_submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        return submit_button.click()
