from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.user.service import UserService
from src.flask.decorator.auth import AuthDecorator


class SendNoticeController(Resource):
    method_decorators = {'put': [AuthDecorator.decorator]}

    def put(self, *args, **kwargs):
        """
            알람 전송
            ---
            description: 알림을 전송합니다.
            tags:
              - friend
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """

        parser = reqparse.RequestParser()
        parser.add_argument('friendUserIdx', location='json')
        parser.add_argument('noticeTypeCode', location='json')
        args1 = parser.parse_args()
        auth = kwargs['user']
        noticeData = {"id": auth["userIdx"]}

        print(args1)
        userService = UserService()
        userService.sendNotice(args1['friendUserIdx'], args1['noticeTypeCode'], noticeData, False)
        return make_response(jsonify(), 200)
