from src.database.database import Database
from src.utils.customError import CustomError
from src.utils.crypto import Crypto
from src.utils.jwt import JWT
from .sql import UserSQL


class UserService:
    def duplicateEmail(self, email):
        result = Database.query(UserSQL.getDuplicateEmail(),
                                {'email': email}).one()
        return result
