from tests.ysemenov.hw6.pages.base_page import BasePage
from tests.ysemenov.hw6.locators import LocatorsCompletePage


class OrderStatusPage(BasePage):

    @property
    def order_msg(self) -> str:
        return self.find_element(*LocatorsCompletePage.HEADER_COMPLETE).text
