from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.diary.service import DiaryService
from src.flask.decorator.auth import AuthDecorator


class DiaryController(Resource):
    method_decorators = {'get': [AuthDecorator.decorator]}

    def get(self, *args, **kwargs):
        """
            일기장 목록 가져오
            ---
            description: 일기장 목록을 가져옵니다.
            tags:
              - diary
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """
        parser = reqparse.RequestParser()
        parser.add_argument('Authorization', location='headers')
        args = parser.parse_args()
        auth = kwargs['user']

        diaryService = DiaryService()
        result = diaryService.getDiaryList(auth['userIdx'])
        print(result)
        return make_response(jsonify(result), 200)
