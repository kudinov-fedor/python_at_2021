class Constants:
    USER_NAME = "User"
    USER_PASS = "Pass123!=="
    BASE_URL = "https://demoqa.com"


class BookStoreEndpoints:
    BOOK_STORE_URL = f"{Constants.BASE_URL}/BookStore/v1/"
    BOOK = f"{BOOK_STORE_URL}Book"
    BOOKS = f"{BOOK_STORE_URL}Books"


class AccountEndpoints:
    ACCOUNT_ENDPOINT = f"{Constants.BASE_URL}/Account/v1/"
    AUTHORIZED = f"{ACCOUNT_ENDPOINT}Authorized"
    GENERATE_TOKEN = f"{ACCOUNT_ENDPOINT}GenerateToken"
    USER = f"{ACCOUNT_ENDPOINT}User"
