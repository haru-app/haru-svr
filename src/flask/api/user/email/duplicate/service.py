from src.database.database import Database
from src.utils.customError import CustomError
from src.utils.crypto import Crypto
from src.utils.jwt import JWT
from .sql import DuplicateEmailSQL


class DuplicateEmailService:
    def duplicateEmail(self, email):
        result = Database.query(DuplicateEmailSQL.getDuplicateEmail(),
                                {'email': email}).one()
        return result
