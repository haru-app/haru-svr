from src.database.database import Database
from src.utils.customError import CustomError
from src.utils.crypto import Crypto
from src.utils.jwt import JWT
from .sql import RegisterSQL


class RegisterService:
    def register(self, email, password, username, birthday):
        count = Database.query(RegisterSQL.register(),
                               {'email': email, 'password': Crypto.sha256(password), 'username': username,
                                'birthday': birthday}).count()

        if count == 0:
            raise CustomError(500, 1000, '중본된 이메일 입니다.')
