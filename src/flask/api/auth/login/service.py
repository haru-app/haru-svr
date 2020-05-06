from src.database.database import Database
from src.utils.customError import CustomError
from src.utils.crypto import Crypto
from src.utils.token import Token
from .sql import LoginSQL


class LoginService:
    def login(self, email, password):
        result = Database.query(LoginSQL.login(), {'email': email, 'password': Crypto.sha256(password)}).one()

        if result is None:
            raise CustomError(1000, '로그인 오류', '일치하는 계정이 없습니다.')

        token = Token()
        accessToken = token.createAccessToken(email, result['userName'])
        refreshToken = token.createRefreshToken(email, result['userName'])
        print(type(accessToken))
        return {'accessToken': accessToken, 'refreshToken': refreshToken}
