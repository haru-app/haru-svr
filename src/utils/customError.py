from werkzeug.exceptions import HTTPException


class CustomError(HTTPException):
    def __init__(self, status=500, code=0, title='시스템 오류', description='알 수 없는 오류가 발생하였습니다.'):
        self.code = code
        self.title = title
        self.description = description
        self.status = status

    def get(self):
        return {'code': self.code,
                'title': self.title,
                'description': self.description}
