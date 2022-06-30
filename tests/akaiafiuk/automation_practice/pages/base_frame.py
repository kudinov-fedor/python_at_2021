from selenium.webdriver.common.by import By
from tests.akaiafiuk.automation_practice.pages.base_page import BasePage


class BaseFrame(BasePage):
    FRAME = By.XPATH, './/iframe[contains(@id, "fancybox")]'
    MODAL = By.XPATH, '//*[@id="product"]'

    def __enter__(self):
        iframe = self.find_element(BaseFrame.FRAME)
        self.session.switch_to.frame(iframe)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.switch_to.default_content()
