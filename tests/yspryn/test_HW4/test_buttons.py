from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC


def test_click(session):
    session.get("https://demoqa.com/buttons")
    session.find_element(By.XPATH, "//button[text()='Click Me']").click()
    assert session.find_element(By.CSS_SELECTOR, "#dynamicClickMessage").text == "You have done a dynamic click"


def test_right_click_button(session):
    session.get("https://demoqa.com/buttons")
    button = session.find_element(By.CSS_SELECTOR, "button#rightClickBtn")
    AC(session).context_click(button).perform()
    assert session.find_element(By.CSS_SELECTOR, "#rightClickMessage").text == "You have done a right click"


def test_double_click_button(session):
    session.get("https://demoqa.com/buttons")
    button = session.find_element(By.CSS_SELECTOR, "button#doubleClickBtn")
    AC(session).double_click(button).perform()
    assert session.find_element(By.CSS_SELECTOR, "#doubleClickMessage").text == "You have done a double click"
