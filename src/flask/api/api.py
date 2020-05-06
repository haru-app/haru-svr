from .user.controller import UserController
from .auth.login.controller import LoginController


class Api:
    def getRouters(self):
        return [
            {'class': UserController, 'path': '/api/user'},
            {'class': LoginController, 'path': '/api/auth/login'}
        ]
