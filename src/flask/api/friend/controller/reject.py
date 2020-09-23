from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.friend.service import FriendService
from src.flask.decorator.auth import AuthDecorator


class RejectFriendRequestController(Resource):
    method_decorators = {'delete': [AuthDecorator.decorator]}

    def delete(self, *args, **kwargs):
        """
            친구 요청 거절
            ---
            description: 친구 요청을 거절합니다.
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
        args = parser.parse_args()
        auth = kwargs['user']

        friendService = FriendService()
        friendService.rejectFriendRequest(args['friendUserIdx'], auth['userIdx'])
        return make_response(jsonify(), 200)
