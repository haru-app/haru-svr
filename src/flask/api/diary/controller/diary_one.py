from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.diary.service import DiaryService
from src.flask.decorator.auth import AuthDecorator


class DiaryOneController(Resource):
    method_decorators = {'delete': [AuthDecorator.decorator]}

    def delete(self, *args, **kwargs):
        """
            일기장 삭제
            ---
            description: 일기장을 삭제합니다.
            tags:
              - diary
            parameters:
              - name: diaryIdx
                description: 이메일
                in: path
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
        parser.add_argument('diaryIdx', location='view_args')
        pargs = parser.parse_args()
        auth = kwargs['user']

        diaryService = DiaryService()
        result = diaryService.removeDiary(auth['userIdx'], pargs['diaryIdx'])

        return make_response(jsonify(result), 200)
