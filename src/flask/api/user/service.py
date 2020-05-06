from src.database.database import Database
from src.utils.customError import CustomError
from src.utils.crypto import Crypto

from .sql import UserSQL


class UserService:
    def register(self, args):
        args['password'] = Crypto.sha256(args['password'])
        count = Database.query(UserSQL.register(), args).count
        if count == 0:
            raise CustomError(1000, '회원가입 오류', '회원가입에 실패하였습니다.')
