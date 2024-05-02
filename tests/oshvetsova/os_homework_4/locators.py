from selenium.webdriver.common.by import By


class Buttons:
    BTN_DOUBLE_CLICK_ME = (By.XPATH, "//*[@id='doubleClickBtn']")
    TXT_DOUBLE_CLICK_ME = (By.XPATH, "//*[@id='doubleClickMessage']")
    BTN_RIGHT_CLICK_ME = (By.XPATH, "//*[@id='rightClickBtn']")
    TXT_RIGHT_CLICK_ME = (By.XPATH, "//*[@id='rightClickMessage']")
    BTN_CLICK_ME = (By.XPATH, "//*[ text()= 'Click Me']")
    TXT_CLICK_ME = (By.XPATH, "//*[@id='dynamicClickMessage']")


class DynamicProperties:
    BTN_TEMP_DISABLED = (By.XPATH, "//*[@id='enableAfter']")
    BTN_COLOR_CHANGE = (By.XPATH, "//*[ text() = 'Color Change']")
    BTN_VISIBLE_AFTER = (By.XPATH, "//*[@id='visibleAfter']")
