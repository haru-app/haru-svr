class CustomError:
    def __init__(self, code=0, title='시스템 오류', detail=''):
        self.code = code
        self.title = title
        self.detail = detail

    def get(self):
        return {'code': self.code, 'title': self.title, 'detail': self.detail}
