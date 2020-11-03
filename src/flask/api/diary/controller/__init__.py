from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.diary.service import DiaryService
from src.flask.decorator.auth import AuthDecorator


class DiaryController(Resource):
    method_decorators = {'get': [AuthDecorator.decorator], 'post': [AuthDecorator.decorator]}

    def get(self, *args, **kwargs):
        """
            일기장 목록 가져오기
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
        auth = kwargs['user']

        diaryService = DiaryService()
        result = diaryService.getDiaryList(auth['userIdx'])
        print(result)
        return make_response(jsonify(result), 200)

    def post(self, *args, **kwargs):
        """
            일기장 추가
            ---
            description: 일기장을 추가합니다.
            tags:
              - diary
            requestBody:
              description: 일기장 구성
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - diaryName
                      - diaryIconCode
                      - publicRangeCode
                    properties:
                      diaryName:
                        diaryName: 일기장 이름
                        type: string
                      diaryIconCode:
                        descripion: 아이콘 코드
                        type: string
                      publicRangeCode:
                        description: 공개범위 코드
                        type: string
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """
        parser = reqparse.RequestParser()
        parser.add_argument('diaryName', location='json')
        parser.add_argument('diaryIconCode', location='json')
        parser.add_argument('publicRangeCode', location='json')
        args = parser.parse_args()

        auth = kwargs['user']

        diaryService = DiaryService()

        result = diaryService.addDiary(auth['userIdx'], args['diaryName'], args['diaryIconCode'],
                                       args['publicRangeCode'])
        print(result)
        return make_response(jsonify(result), 200)
