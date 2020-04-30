from .user.controller import UserController


class Api:
    def __init__(self):
        self.controllers = [
            {
                'class': UserController,
                'path': '/user'
            }
        ]

    def getControllers(self):
        return self.controllers
