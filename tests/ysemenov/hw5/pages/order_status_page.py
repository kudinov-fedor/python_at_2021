from tests.ysemenov.hw5.pages.base_page import BasePage
from tests.ysemenov.hw5.locators import LocatorsCompletePage


class OrderStatusPage(BasePage):

    def get_order_msg(self) -> str:
        return self.find_element(*LocatorsCompletePage.HEADER_COMPLETE).text
