from flask_restful import Resource, reqparse
from flask import jsonify, make_response

from src.flask.api.auth.service import AuthService


class LoginController(Resource):
    def post(self, *args, **kwargs):
        """
            로그인
            ---
            description: 로그인을 합니다.
            tags:
              - auth
            requestBody:
              description: 로그인 내용
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - email
                      - password
                    properties:
                      email:
                        description: 이메일
                        type: string
                      password:
                        description: 비밀번호
                        type: string
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='json')
        parser.add_argument('password', location='json')
        args = parser.parse_args()

        authService = AuthService()
        data = authService.login(args['email'], args['password'])
        return make_response(jsonify(data), 200)
