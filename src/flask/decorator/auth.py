from flask_restful import reqparse, abort
from flask import jsonify, make_response
from functools import wraps
from src.utils.customError import CustomError
from src.utils.jwt import JWT


class AuthDecorator:
    @staticmethod
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            parser = reqparse.RequestParser()
            parser.add_argument('Authorization', location='headers')
            args = parser.parse_args()
            if args['Authorization'] is None or args['Authorization'].startswith('bearer ') is False:
                raise CustomError(401, 1000, '인증 오류', '로그인을 먼저 해야합니다.')

            accessToken = args['Authorization'][7:]

            jwt = JWT()
            token = jwt.validToken(accessToken)
            print(token)
            kwargs['user'] = token
            if token is None:
                raise CustomError(401, 1001, '인증 오류', '인증이 만료되었습니다.')

            return func(*args, **kwargs)

        return wrapper
