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
            parameters:
              - name: email
                description: 이메일
                in: query
                schema:
                  type: string
                required: true
              - name: password
                description: 비밀번호
                in: query
                schema:
                  type: string
                required: true
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
