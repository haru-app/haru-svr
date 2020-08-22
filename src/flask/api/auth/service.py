from src.database.database import Database
from src.utils.customError import CustomError
from src.utils.crypto import Crypto
from src.utils.jwt import JWT
from .sql import AuthSQL
from src.flask.api.user.service import UserService


class AuthService:
    def login(self, email, password):
        result = Database.query(AuthSQL.login(), {'email': email, 'password': Crypto.sha256(password)}).one()

        if result is None:
            raise CustomError(500, 1000, '일치하는 계정이 없습니다.')

        jwt = JWT()
        accessToken = jwt.createAccessToken(result['userIdx'], email, result['username'])
        refreshToken = jwt.createRefreshToken(result['userIdx'], email, result['username'])

        self.updateRefreshToken(refreshToken, email)

        return {'accessToken': accessToken, 'refreshToken': refreshToken, **result}

    def register(self, email, password, username, birthday):
        userService = UserService()

        if userService.duplicateEmail(email)['isDuplicateEmail']:
            raise CustomError(500, 1000, '중본된 이메일 입니다.')

        Database.query(AuthSQL.register(),
                       {'email': email, 'password': Crypto.sha256(password), 'username': username,
                        'birthday': birthday})

    def updateToken(self, accessToken, refreshToken):
        jwt = JWT()
        rt = jwt.validToken(refreshToken)
        if rt is None:
            raise CustomError(500, 1002, '인증이 만료되어 다시 로그인 해야합니다.')

        at = jwt.decodeToken(accessToken)
        if at is None or rt['userIdx'] != at['userIdx'] or rt['email'] != at['email']:
            raise CustomError(500, 1002, '인증이 만료되어 다시 로그인 해야합니다.')

        newAccessToken = jwt.createAccessToken(rt['userIdx'], rt['email'], rt['username'])
        # self.updateRefreshToken(newRefreshToken, rt['email'])

        return {'accessToken': newAccessToken, 'email': at['email'], 'username': at['username']}

    def updateRefreshToken(self, token, email):
        def transFunc(query, commit, rollback):
            count = query(AuthSQL.updateRefreshToken(), {'refreshToken': token, 'email': email})
            if count == 0:
                raise CustomError()
            count = query(AuthSQL.updateUpdateTime(), {'email': email})
            if count == 0:
                raise CustomError()
            commit()

        Database.transaction(transFunc)
