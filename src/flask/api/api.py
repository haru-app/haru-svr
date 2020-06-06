from .auth.register.controller import RegisterController
from .user.controller import UserController
from .auth.login.controller import LoginController
from .user.email.duplicate.controller import DuplicateEmailController


class Api:
    def getRouters(self):
        return [
            {'class': DuplicateEmailController, 'path': '/api/user/email/duplicate'},
            {'class': UserController, 'path': '/api/user'},
            {'class': LoginController, 'path': '/api/auth/login'},
            {'class': RegisterController, 'path': '/api/auth/register'}
        ]
