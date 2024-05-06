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
    DIV_DRAGGABLE_SIMPLE = (By.XPATH, "//div[@id='simpleDropContainer']//p")
    DIV_DROPPABLE_SIMPLE = (By.XPATH, "//div[@id='simpleDropContainer']//div[@id='draggable']")
    TXT_DROPPABLE_SIMPLE = (By.XPATH, "//div[@id='simpleDropContainer']//div[@id='droppable'")
