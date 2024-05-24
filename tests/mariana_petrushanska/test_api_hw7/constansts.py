class General:
    HOST = "https://demoqa.com"
    GENERATE_TOKEN = HOST + "/Account/v1/GenerateToken"


class User:
    USER_NAME = "jane_austen"
    USER_PASSWORD = "PassWord12!"
    USER_ACCOUNT = General.HOST + "/Account/v1/User"
    USER_LOGIN = General.HOST + "/Account/v1/Login"
    USER_AUTHORIZED = General.HOST + "/Account/v1/Authorized"


class Books:
    BOOK_LIST = General.HOST + "/BookStore/v1/Books"
    BOOK = General.HOST + "/BookStore/v1/Book"
    BOOK_ISBN = "9781449331818"
