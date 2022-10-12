from selenium.webdriver.common.by import By

DELETE_ALL_BOOKS_BUTTON = By.XPATH, "//button[text()='Delete All Books']"


def book_item_delete_icon(book_name: str):
    return By.XPATH, f"//div[@class='rt-td' and contains(.,'{book_name}')]/following-sibling::div//span[" \
                     f"@id='delete-record-undefined'] "
