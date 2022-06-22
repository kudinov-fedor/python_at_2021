from requests import session


class ApiClientBookStore:

    HOST = "https://demoqa.com"

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.session = session()

    def create_user(self):
        path = '/Account/v1/User'
        payload = {"userName": self.login,
                   "password": self.password}
        response = self.session.post(url=f'{self.HOST}{path}',
                                     json=payload)
        return response

    def get_user_info(self, user_id):
        path = f'/Account/v1/User{user_id}'
        response = self.session.get(url=f'{self.HOST}{path}')
        return response

    def login_user(self):
        path = '/Account/v1/Authorized'
        payload = {"userName": self.login,
                   "password": self.password}
        response = self.session.post(url=f'{self.HOST}{path}',
                                     json=payload)
        return response

    def delete_account(self, user_id):
        path = f'/Account/v1/User{user_id}'
        response = self.session.delete(url=f'{self.HOST}{path}')
        return response

    def generate_token(self):
        path = '/Account/v1/GenerateToken'
        payload = {"userName": self.login,
                   "password": self.password}
        response = self.session.post(url=f'{self.HOST}{path}',
                                     json=payload)
        return response

    def get_books(self):
        path = '/BookStore/v1/Books'
        response = self.session.get(url=f'{self.HOST}{path}')
        return response

    def add_book(self, user_id, isbn):
        path ='/BookStore/v1/Books'
        payload = {"userId": user_id,
                   "collectionOfIsbns": [
                       {"isbn": isbn}]
                   }
        response = self.session.post(url=f'{self.HOST}{path}',
                                     json=payload)
        return response
