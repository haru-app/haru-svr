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
            description: 알람을 전송합니다.
            tags:
              - friend
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """

        parser = reqparse.RequestParser()
        parser.add_argument('friendUserIdx', location='view_args')
        parser.add_argument('noticeTypeCode', location='view_args')
        parser.add_argument('noticeData', location='view_args')
        parser.add_argument('isCheck', location='view_args')
        args1 = parser.parse_args()
        auth = kwargs['user']

        userService = UserService()
        userService.sendNotice(args1['friendUserIdx'], args1['noticeTypeCode'], args1['noticeData'], args1['isCheck'])
        return make_response(jsonify(), 200)
