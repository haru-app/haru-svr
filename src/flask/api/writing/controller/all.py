from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from src.flask.api.writing.service import WritingService
from src.flask.decorator.auth import AuthDecorator
from src.utils.validator import Validator


class WritingAllController(Resource):
    method_decorators = {'get': [AuthDecorator.decorator]}

    def get(self, *args, **kwargs):
        """
            일기 불러오기
            ---
            description: 일기를 불러옵니다.
            tags:
              - writing
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """
        writingService = WritingService(kwargs['user'])

        result = writingService.getWritingAll()
        print(result)
        return make_response(jsonify(result), 200)
