from werkzeug.exceptions import HTTPException


class CustomError(HTTPException):
    def __init__(self, status=500, code=0, errorMessage='알 수 없는 오류가 발생하였습니다.', detail=None):
        self.code = code
        self.errorMessage = errorMessage
        self.detail = detail
        self.status = status

    def get(self):
        return {'code': self.code,
                'errorMessage': self.errorMessage,
                'detail': self.detail}
