from flask_restful import Resource, reqparse
from flask import jsonify, make_response

from src.utils.validator import Validator
from .service import DuplicateEmailService


class DuplicateEmailController(Resource):
    def get(self):
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
        args = parser.parse_args()

        duplicateEmailService = DuplicateEmailService()
        result = duplicateEmailService.duplicateEmail(args['email'])
        return make_response(jsonify(result), 200)
