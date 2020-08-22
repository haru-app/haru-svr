import jwt
from datetime import datetime, timedelta
from src.config import Config


class JWT:
    def __init__(self):
        super().__init__()
        self.jwtSecret = Config.getConfig()['key']['jwtSecret']
        self.algorithm = "HS256"

    # Access Token 생성
    def createAccessToken(self, userIdx, email, username):
        data_to_encode = {'userIdx': userIdx, 'email': email, 'username': username,
                          'exp': datetime.now().utcnow() + timedelta(hours=1),
                          'iat': datetime.now()}
        token = jwt.encode(data_to_encode, self.jwtSecret, algorithm=self.algorithm)
        return token.decode('utf-8')

    # Refresh Token 생성
    def createRefreshToken(self, userIdx, email, username):
        data_to_encode = {'userIdx': userIdx, 'email': email, 'username': username,
                          'exp': datetime.now().utcnow() + timedelta(days=30),
                          'iat': datetime.now()}
        token = jwt.encode(data_to_encode, self.jwtSecret, algorithm=self.algorithm)
        return token.decode('utf-8')

    # Token 검증
    def validToken(self, token):
        try:
            t = jwt.decode(token, self.jwtSecret, algorithms=[self.algorithm])
        except jwt.ExpiredSignatureError:
            return None
        return t

    # Token 검증 안하고 복호화
    def decodeToken(self, token):
        try:
            t = jwt.decode(token, self.jwtSecret, algorithms=[self.algorithm], verify=False)
        except:
            return None
        return t
