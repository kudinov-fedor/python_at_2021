from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from tests.ylond.pageObject.base_page import BasePage, BaseElement


class WebPages(BasePage):
    URL = "/webtables"

    # locators
    add_button = By.ID, "addNewRecordButton"

    def get_fill_form(self):
        self.find_element(*self.add_button).click()
        return CreateUserForm(self.driver)

    def get_pop_up(self):
        return CreateUserForm(self.driver)

    def get_web_table(self):
        return WebTable(self.driver)


class CreateUserForm(BaseElement):

    ROOT_ELEMENT = By.ID, "userForm"

    # locators
    first_name = By.ID, "firstName"
    last_name = By.ID, "lastName"
    email = By.ID, "userEmail"
    age = By.ID, "age"
    salary = By.ID, "salary"
    department = By.ID, "department"
    modal_window = By.ID, "userForm"

    # buttons
    cancel_button = By.CSS_SELECTOR, "button.close"
    submit_button = By.CSS_SELECTOR, "button#submit"

    def enter_first_name(self, firstName: str):
        self.find_element(*self.first_name).send_keys(firstName)
        return self

    def enter_last_name(self, lastName: str):
        self.find_element(*self.last_name).send_keys(lastName)
        return self

    def enter_email(self, email: str):
        self.find_element(*self.email).send_keys(email)
        return self

    def enter_age(self, age: str):
        self.find_element(*self.age).send_keys(age)
        return self

    def enter_salary(self, salary: str):
        self.find_element(*self.salary).send_keys(salary)
        return self

    def enter_department(self, department: str):
        self.find_element(*self.department).send_keys(department)
        return self

    def click_submit_button(self):
        self.find_element(*self.submit_button).click()
        return self

    def clear_all(self):
        locators = [self.first_name,
                    self.last_name,
                    self.email,
                    self.age,
                    self.salary,
                    self.department]
        for locator in locators:
            self.find_element(*locator).clear()
        return self

    def employee_registration(self, first_name: str = '', last_name: str = '', email: str = '',
                                  salary: str = '', age: str = '', department: str = ''):
        self.clear_all()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_salary(salary)
        self.enter_age(age)
        self.enter_department(department)
        self.click_submit_button()
        return self

    def edit_employee(self, first_name: str = ''):
        self.find_element(*self.first_name).clear()
        self.enter_first_name(first_name)
        self.click_submit_button()
        return self


class WebTable(BaseElement):

    ROOT_ELEMENT = By.CSS_SELECTOR, "div.rt-table"

    # locators
    search = By.CSS_SELECTOR, "input#searchBox.form-control"
    grid = By.CSS_SELECTOR, "div.rt-tbody"

    # buttons
    remove_button = By.CSS_SELECTOR, "span#delete-record-1"
    edit_button = By.CSS_SELECTOR, "span#edit-record-1.mr-2"

    # pagination
    pagination_total_pages = By.CSS_SELECTOR, "span.-totalPages"
    pagination_current_pages = By.XPATH, "//input[@aria-label= 'jump to page']"

    # grid result
    first_name_result = By.CSS_SELECTOR, "div.rt-td"
    new_grid_row = By.CSS_SELECTOR, "div.rt-tr.-padRow.-even"

    def get_first_name_result(self) -> str:
        get_first_name_result = self.root_element.find_element(*self.first_name_result).text
        return get_first_name_result

    def get_employee_register_result(self) -> bool:
        if self.find_element(*self.new_grid_row).text != '':
            return True

    def is_remove_button_present(self) -> bool:
        try:
            self.find_element(*self.remove_button)
        except NoSuchElementException:
            return False
        return True

    def is_edit_button_present(self) -> bool:
        try:
            self.find_element(*self.edit_button)
        except NoSuchElementException:
            return False
        return True

    def click_edit_button(self):
        self.find_element(*self.edit_button).click()
        return self

    def click_remove_button(self):
        self.find_element(*self.remove_button).click()
        return self

    def remove_employee(self):
        if self.find_element(*self.remove_button) is not None:
            self.click_remove_button()
        else:
            print("No remove button")

    def search_employee_by_first_name(self, first_name: str):
        self.find_element(*self.search).send_keys(first_name)
        return self

    def get_total_pages(self) -> str:
        get_total_pages = self.find_element(*self.pagination_total_pages).text
        return get_total_pages
