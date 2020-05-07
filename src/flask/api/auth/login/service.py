from src.database.database import Database
from src.utils.customError import CustomError
from src.utils.crypto import Crypto
from src.utils.jwt import JWT
from .sql import LoginSQL


class LoginService:
    def login(self, email, password):
        result = Database.query(LoginSQL.login(), {'email': email, 'password': Crypto.sha256(password)}).one()

        if result is None:
            raise CustomError(1000, '로그인 오류', '일치하는 계정이 없습니다.')

        jwt = JWT()
        accessToken = jwt.createAccessToken(email, result['userName'])
        refreshToken = jwt.createRefreshToken(email, result['userName'])

        self.updateRefreshToken(refreshToken, email)

        return {'accessToken': accessToken}

    def updateRefreshToken(self, token, email):
        count = Database.query(LoginSQL.updateRefreshToken(), {'refreshToken': token, 'email': email}).count()
        if count == 0:
            raise CustomError()
