from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.friend.service import FriendService
from src.flask.decorator.auth import AuthDecorator


class CheckFriendController(Resource):
    method_decorators = {'get': [AuthDecorator.decorator]}

    def get(self, *args, **kwargs):
        """
            친구 여부 확인
            ---
            description: 친구 여부를 확인합니다.
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
        result = friendService.checkFriend(auth['userIdx'], args['friendUserIdx'])
        if not result:
            result = [{'useridx': None, 'frienduseridx': None, 'useridx2': None, 'frienduseridx2': None}]
        print(result)
        return make_response(jsonify(result), 200)
