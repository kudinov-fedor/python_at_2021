from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.full_name_text = ""
        self.email_text = ""
        self.current_address_text = ""
        self.permanent_address_text = ""
