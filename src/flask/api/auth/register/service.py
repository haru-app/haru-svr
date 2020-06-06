from src.database.database import Database
from src.utils.customError import CustomError
from src.utils.crypto import Crypto
from .sql import RegisterSQL
from src.flask.api.user.email.duplicate.service import DuplicateEmailService


class RegisterService:
    def register(self, email, password, username, birthday):
        duplicateEmailService = DuplicateEmailService()

        if duplicateEmailService.duplicateEmail(email)['isDuplicateEmail']:
            raise CustomError(500, 1000, '중본된 이메일 입니다.')

        Database.query(RegisterSQL.register(),
                       {'email': email, 'password': Crypto.sha256(password), 'username': username,
                        'birthday': birthday})
