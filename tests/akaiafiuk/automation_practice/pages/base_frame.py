from tests.akaiafiuk.automation_practice.pages.base_page import BasePage


class BaseFrame(BasePage):
    FRAME = None

    def __enter__(self):
        assert self.FRAME is not None
        iframe = self.find_element(self.FRAME)
        self.session.switch_to.frame(iframe)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.switch_to.default_content()
