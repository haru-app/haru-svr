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
            try:
                parser = reqparse.RequestParser()
                parser.add_argument('Authorization', location='headers')
                args = parser.parse_args()

                if args['Authorization'] is None or args['Authorization'].startswith('bearer ') is False:
                    return make_response(jsonify(CustomError(1000, '인증 오류', '로그인을 먼저 해야합니다.').get()), 401)

                accessToken = args['Authorization'][7:]

                jwt = JWT()
                token = jwt.validToken(accessToken)
                if token is None:
                    return make_response(jsonify(CustomError(1001, '인증 오류', '인증이 만료되었습니다.').get()), 401)

            except Exception as err:
                return make_response(jsonify(CustomError(detail=str(err)).get()), 500)

            return func(*args, **kwargs)

        return wrapper
