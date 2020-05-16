from src.utils.customError import CustomError


class ErrorHandler(BaseException):
    status = 500
    message = 'Internal Error'
    extras = None

    @property
    def custom_data(self):
        print('에러핸들러 작동')
        return {k: getattr(self, k) for k in ['status', 'message', 'extras'] if getattr(self, k)}
