from selenium.webdriver.common.by import By


class LandingPage:
    inpt_full = (By.CSS_SELECTOR, "input#userName.mr-sm-2.form-control")
    inpt_email = (By.CSS_SELECTOR, "input#userEmail.mr-sm-2.form-control")
    inpt_cur_addr = (By.CSS_SELECTOR, "textarea#currentAddress.form-control")
    inpt_perm_addr = (By.CSS_SELECTOR, "textarea#permanentAddress.form-control")
    sbmt_button = (By.CSS_SELECTOR, "button#submit.btn.btn-primary")
