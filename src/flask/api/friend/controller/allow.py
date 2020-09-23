from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.friend.service import FriendService
from src.flask.decorator.auth import AuthDecorator


class AllowFriendRequestController(Resource):
    method_decorators = {'put': [AuthDecorator.decorator]}

    def put(self, *args, **kwargs):
        """
            친구 요청 수락
            ---
            description: 친구 요청을 수락합니다.
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
        args1 = parser.parse_args()
        auth = kwargs['user']

        friendService = FriendService()
        friendService.allowFriendRequest(auth['userIdx'], args1['friendUserIdx'])
        return make_response(jsonify(), 200)
