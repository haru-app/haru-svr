from werkzeug.exceptions import HTTPException


class CustomError(HTTPException):
    def __init__(self, code=0, title='시스템 오류', description=''):
        self.code = code
        self.title = title
        self.description = description

    def get(self):
        return {'code': self.code, 'title': self.title, 'detail': self.detail}
