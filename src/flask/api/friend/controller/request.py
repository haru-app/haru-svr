from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.friend.service import FriendService
from src.flask.decorator.auth import AuthDecorator


class FriendRequestController(Resource):
    method_decorators = {'get': [AuthDecorator.decorator]}

    def get(self, *args, **kwargs):
        """
            친구 불러오기
            ---
            description: 친구 목록을 가져옵니다.
            tags:
              - friend
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        auth = kwargs['user']

        friendService = FriendService()
        result = friendService.getFriendRequestList(auth['userIdx'])
        print(result)
        return make_response(jsonify(result), 200)
