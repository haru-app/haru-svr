from datetime import datetime

from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request

from src.utils.validator import Validator
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
                      username:
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
        print(request.data);
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='json')
        parser.add_argument('password', location='json')
        parser.add_argument('username', location='json')
        parser.add_argument('birthday', location='json')
        args = Validator.validate(
            {'email': Validator.email(),
             'password': Validator.password(),
             'username': Validator.username(),
             'birthday': Validator.birthday()}, parser.parse_args())

        registerService = RegisterService()
        registerService.register(args['email'], args['password'], args['username'], args['birthday'])
        return make_response(jsonify(), 200)
