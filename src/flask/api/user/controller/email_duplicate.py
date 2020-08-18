from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.user.service import UserService
from src.flask.decorator.auth import AuthDecorator


class EmailDuplicateController(Resource):
    method_decorators = {'get': [AuthDecorator.decorator]}

    def get(self, *args, **kwargs):
        """
            이메일 중복 체크
            ---
            description: 이메일 중복 체크 합니다.
            tags:
              - user
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
        parser.add_argument('email', location='args')
        parser.add_argument('Authorization', location='headers')
        parser.add_argument('Content-Type', location='headers')
        args = parser.parse_args()
        print(args['Authorization'])
        print(kwargs)
        userService = UserService()
        result = userService.duplicateEmail(args['email'])
        return make_response(jsonify(result), 200)
