from src.flask.api.auth.controller.register import RegisterController
from src.flask.api.auth.controller.token import TokenController
from src.flask.api.auth.controller.login import LoginController
from .code.controller.all import AllCodeController
from .user.controller.email_duplicate import EmailDuplicateController
from .diary.controller import DiaryController


class Api:
    def getRouters(self):
        return [
            {'class': LoginController, 'path': '/api/auth/login'},
            {'class': RegisterController, 'path': '/api/auth/register'},
            {'class': TokenController, 'path': '/api/auth/token'},
            {'class': EmailDuplicateController, 'path': '/api/user/email/duplicate'},
            {'class': AllCodeController, 'path': '/api/code/all'},
            {'class': DiaryController, 'path': '/api/diary'},
        ]
