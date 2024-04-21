from selenium.webdriver.common.by import By


class DynamicProperties:
    BTN_DISABLED = (By.XPATH, "//*[@id='enableAfter']")
    BTN_COLOR_CHANGE = (By.XPATH, "//*[contains(@class, 'text-danger')]")
    BTN_VISIBLE_AFTER = (By.XPATH, "//*[@id='visibleAfter']")


class ButtonsPage:
    BTN_DOUBLE_CLICK = (By.XPATH, "//*[@id='doubleClickBtn']")
    BTN_RIGHT_CLICK = (By.XPATH, "//*[@id='rightClickBtn']")
    BTN_DYNAMIC_CLICK = (By.XPATH, "//*[ text()= 'Click Me']")
    TXT_DOUBLE_CLICK = (By.XPATH, "//*[@id='doubleClickMessage']")
    TXT_RIGHT_CLICK = (By.XPATH, "//*[@id='rightClickMessage']")
    TXT_DYNAMIC_CLICK = (By.XPATH, "//*[@id='dynamicClickMessage']")
