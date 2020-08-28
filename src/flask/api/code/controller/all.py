from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.code.service import CodeService
from src.flask.decorator.auth import AuthDecorator


class AllCodeController(Resource):
    method_decorators = {'get': [AuthDecorator.decorator]}

    def get(self, *args, **kwargs):
        """
            모든 코드 불러오기
            ---
            description: 모든 코드를 불러옵니다.
            tags:
              - code
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """
        codeService = CodeService()
        result = codeService.getAllCode()
        print(result)
        return make_response(jsonify(result), 200)
