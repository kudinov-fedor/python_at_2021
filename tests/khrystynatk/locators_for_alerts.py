from selenium.webdriver.common.by import By


class LandingPage:
    alerts_wrapper = (By.CSS_SELECTOR, "div#javascriptAlertsWrapper")
    alert_button = (By.CSS_SELECTOR, "#alertButton")
    wait_alert_button = (By.CSS_SELECTOR, "#timerAlertButton")
    confirm_alert_button = (By.CSS_SELECTOR, "#confirmButton")
    prompt_box_button = (By.CSS_SELECTOR, "#promtButton")


class Result:
    confirm_alert_res = (By.CSS_SELECTOR, "#confirmResult")
    prompt_box_res = (By.CSS_SELECTOR, "#promptResult")
