from selenium.webdriver.common.by import By


class DynamicPage:
    BTN_ENABLED = By.XPATH, ".//*[@id='enableAfter']"
    BTN_COLOR = By.XPATH, ".//button[@id='colorChange' and contains(@class, 'text-danger')]"
    BTN_VISIBLE = By.ID, "visibleAfter"


class ButtonsPage:
    BTN_DBL_CLICK = By.CSS_SELECTOR, "#doubleClickBtn"
    MSG_DBL_CLICK = By.CSS_SELECTOR, "#doubleClickMessage"
    BTN_RIGHT_CLICK = By.CSS_SELECTOR, "#rightClickBtn"
    MSG_RIGHT_CLICK = By.CSS_SELECTOR, "#rightClickMessage"
    BTN_DYN_CLICK = By.XPATH, ".//*[@class='btn btn-primary' and text()='Click Me']"
    MSG_DYN_CLICK = By.CSS_SELECTOR, "#dynamicClickMessage"


class DroppablePage:
    DRAG_BOX = By.CSS_SELECTOR, "#draggable"
    DROP_BOX = By.CSS_SELECTOR, "#droppable"
    DROPPED_TEXT = By.XPATH, "//*[@id='droppable']//p[text()='Dropped!']"
