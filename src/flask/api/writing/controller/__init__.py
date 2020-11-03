from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from src.flask.api.writing.service import WritingService
from src.flask.decorator.auth import AuthDecorator
from src.utils.validator import Validator


class WritingController(Resource):
    method_decorators = {'get': [AuthDecorator.decorator], 'post': [AuthDecorator.decorator]}

    def post(self, *args, **kwargs):
        """
            일기 작성
            ---
            description: 일기를 작성합니다.
            tags:
              - writing
            requestBody:
              description: 일기 작성
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - diaryIdx
                      - title
                      - content
                      - score
                    properties:
                      diaryIdx:
                        description: 일기장 Idx
                        type: integer
                      writingDate:
                        description: 작성 날짜
                        type: string
                      title:
                        description: 제목
                        type: string
                      content:
                        description: 내용
                        type: string
                      score:
                        description: 평점
                        type: integer
                      writingTags:
                        description: 해시태그
                        type: array
                        items:
                          type: string
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """
        print(request.json)
        args = Validator.validate(
            {'diaryIdx': {'type': 'integer'},
             'writingDate': {'type': 'datetime', 'coerce': 'utcDatetime'},
             'title': {'type': 'string'},
             'content': {'type': 'string'},
             'score': {'type': 'integer'},
             'writingTags': {'type': 'list', 'schema': {'type': 'string'}, 'required': False}
             }, request.json)
        auth = kwargs['user']
        writingService = WritingService(kwargs['user'])

        result = writingService.addWriting(args['diaryIdx'], args['writingDate'], args['title'],
                                           args['content'], args['score'], args['writingTags'])

        return make_response(jsonify(result), 200)

    def get(self, *args, **kwargs):
        """
            일기 불러오기
            ---
            description: 일기를 불러옵니다.
            tags:
              - writing
            parameters:
              - name: diaryIdx
                description: 이메일 idx
                in: query
                schema:
                  type: int
                required: true
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """
        parser = reqparse.RequestParser()
        parser.add_argument('diaryIdx', location='args')
        args = Validator.validate(
            {'diaryIdx': {'type': 'integer', 'coerce': int}}, parser.parse_args())

        writingService = WritingService(kwargs['user'])

        result = writingService.getWriting(args['diaryIdx'])
        print(result)
        return make_response(jsonify(result), 200)
