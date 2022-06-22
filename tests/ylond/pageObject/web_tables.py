from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from tests.ylond.pageObject.base_page import BasePage


class WebTables(BasePage):
    URL = "/webtables"

    # LOCATORS
    # registration_form_id
    first_name = By.ID, "firstName"
    last_name = By.ID, "lastName"
    email = By.ID, "userEmail"
    age = By.ID, "age"
    salary = By.ID, "salary"
    department = By.ID, "department"

    search = By.CSS_SELECTOR, "input#searchBox.form-control"
    grid = By.CSS_SELECTOR, "div.rt-tbody"
    modal_window = By.ID, "userForm"

    #pagination
    pagination_total_pages = By.CSS_SELECTOR, "span.-totalPages"
    pagination_current_pages = By.XPATH, "//input[@aria-label= 'jump to page']"

    # buttons
    add_button = By.ID, "addNewRecordButton"
    submit_button = By.CSS_SELECTOR, "button#submit"
    remove_button = By.CSS_SELECTOR, "span#delete-record-1"
    edit_button = By.CSS_SELECTOR, "span#edit-record-1.mr-2"
    cancel_button = By.CSS_SELECTOR, "button.close"

    # grid result
    first_name_result = By.CSS_SELECTOR, "div.rt-td"
    new_grid_row = By.CSS_SELECTOR, "div.rt-tr.-padRow.-even"

    # FIELDS SETUP
    def get_first_name_result(self) -> str:
        get_first_name_result = self.find_element(*self.first_name_result).text
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

    def enter_first_name(self, firstName):
        enter_first_name = self.find_element(*self.first_name).send_keys(firstName)
        return self

    def enter_last_name(self, lastName):
        enter_last_name = self.find_element(*self.last_name).send_keys(lastName)
        return self

    def enter_email(self, email):
        enter_email = self.find_element(*self.email).send_keys(email)
        return self

    def enter_age(self, age):
        enter_age = self.find_element(*self.age).send_keys(age)
        return self

    def enter_salary(self, salary):
        enter_salary = self.find_element(*self.salary).send_keys(salary)
        return self

    def enter_department(self, department):
        enter_department = self.find_element(*self.department).send_keys(department)
        return self

    def click_add_button(self):
        add_button = self.find_element(*self.add_button).click()
        return self

    def click_edit_button(self):
        edit_button = self.find_element(*self.edit_button).click()
        return self

    def click_submit_button(self):
        submit_button = self.find_element(*self.submit_button).click()
        return self

    def click_remove_button(self):
        remove_button = self.find_element(*self.remove_button).click()
        return self

    # ACTIONS
    def clear_all(self):
        self.find_element(*self.first_name).clear()
        self.find_element(*self.last_name).clear()
        self.find_element(*self.email).clear()
        self.find_element(*self.age).clear()
        self.find_element(*self.salary).clear()
        self.find_element(*self.department).clear()
        return self

    def employee_registration(self, first_name: str = None, last_name: str = None, email: str = None,
                              salary: str = None, age: str = None, department: str = None):
        self.click_add_button()
        self.clear_all()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_salary(salary)
        self.enter_age(age)
        self.enter_department(department)
        self.click_submit_button()
        return self

    def edit_employee(self, first_name: str = None):
        if self.find_element(*self.edit_button) is not None:
            self.click_edit_button()
            self.find_element(*self.first_name).clear()
            self.enter_first_name(first_name)
            self.click_submit_button()
        else:
            self.employee_registration("test", "test1", "abc@gmail.com", "5000", "50", "department")
            self.click_edit_button()
            self.find_element(*self.first_name).clear()
            self.enter_first_name(first_name)
            self.click_submit_button()

    def remove_employee(self):
        if self.find_element(*self.remove_button) is not None:
            self.click_remove_button()
        else:
            print("No remove button")

    def search_employee_by_first_name(self, first_name):
        self.find_element(*self.search).send_keys(first_name)
        return self

    def get_total_pages(self):
        get_total_pages = self.find_element(*self.pagination_total_pages).text
        return get_total_pages
