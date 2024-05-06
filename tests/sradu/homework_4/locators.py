from selenium.webdriver.common.by import By


class SideMenuLocators:
    LIST_MENU_ITEM = (By.XPATH, "//div[contains(@class, 'top-card')]")
    LIST_MENU_SUB_ITEM = (By.XPATH, "//div[@class='element-group']//li")


class AlertsLocators:

    @classmethod
    def get_click_btn_for_item(cls, item_text: str) :
        xpath = (f"//div[@id='javascriptAlertsWrapper']//span[text()='{item_text}']"
                 f"/ancestor::div[contains(@class,'row')][1]//button")
        return By.XPATH, xpath

    @classmethod
    def get_alert_result(cls, item_text: str):
        xpath = (f"//div[@id='javascriptAlertsWrapper']//span[text()='{item_text}']"
                 f"/following-sibling::span[@id='confirmResult']")
        return By.XPATH, xpath


class DragAndDropLocators:

    @classmethod
    def get_locator_for_droppable_text_element(cls, div_id):
        return By.XPATH, f"//div[@id='{div_id}']//p"

    @classmethod
    def get_locator_for_draggable_element(cls, div_id):
        return By.XPATH, f"//div[@id='{div_id}']//div[@id='draggable']"

    @classmethod
    def get_locator_for_droppable_element(cls, div_id):
        return By.XPATH, f"//div[@id='{div_id}']//div[@id='droppable']"

