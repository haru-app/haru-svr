from src.database.database import Database
from src.utils.customError import CustomError
from src.utils.crypto import Crypto
from src.utils.jwt import JWT
from .sql import LoginSQL


class LoginService:
    def login(self, email, password):
        result = Database.query(LoginSQL.login(), {'email': email, 'password': Crypto.sha256(password)}).one()

        if result is None:
            raise CustomError(500, 1000, '일치하는 계정이 없습니다.')

        jwt = JWT()
        accessToken = jwt.createAccessToken(email, result['username'])
        refreshToken = jwt.createRefreshToken(email, result['username'])

        def transFunc(query, commit, rollback):
            count = query(LoginSQL.updateRefreshToken(), {'refreshToken': refreshToken, 'email': email})
            if count == 0:
                raise CustomError()
            count = query(LoginSQL.updateUpdateTime(), {'refreshToken': refreshToken, 'email': email})
            if count == 0:
                raise CustomError()
            commit()

        Database.transaction(transFunc)
        
        return {'accessToken': accessToken, 'refreshToken': refreshToken, **result}

    def updateRefreshToken(self, token, email):
        count = Database.query(LoginSQL.updateRefreshToken(), {'refreshToken': token, 'email': email}).count()
        if count == 0:
            raise CustomError()
