from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from .service import RegisterService


class RegisterController(Resource):
    def post(self):
        """
            회원가입
            ---
            description: 회원가입을 합니다.
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
                      - userName
                      - birthday
                    properties:
                      email:
                        description: 이메일
                        type: string
                      password:
                        description: 비밀번호
                        type: string
                      userName:
                        description: 사용자 이름
                        type: string
                      birthday:
                        description: 생년월일
                        type: string
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='args', required=True, type=str)
        parser.add_argument('password', location='args', required=True, type=str)
        parser.add_argument('username', location='args', required=True, type=str)
        parser.add_argument('birthday', location='args', required=True, type=str)
        args = parser.parse_args()
        loginService = RegisterService()
        data = loginService.login(args['email'], args['password'])
        return make_response(jsonify(data), 200)
