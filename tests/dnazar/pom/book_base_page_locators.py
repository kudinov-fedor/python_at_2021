from selenium.webdriver.common.by import By

SEARCH_INPUT = By.ID, "searchBox"
ADD_TO_COLLECTION_BUTTON = By.XPATH, "//button[text()='Add To Your Collection']"
BACK_TO_STORE_BUTTON = By.XPATH, "//button[text()='Back To Book Store']"
BOOK_ITEMS = By.XPATH, "//img/ancestor::div[contains(@class, 'rt-tr-group')]"


def book_item_link(book_name: str):
    return By.XPATH, f"//a[text()='{book_name}']"
