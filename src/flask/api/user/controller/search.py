from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from src.flask.api.user.service import UserService
from src.flask.decorator.auth import AuthDecorator


class SearchUserController(Resource):
    method_decorators = {'get': [AuthDecorator.decorator]}

    def get(self, *args, **kwargs):
        """
            유저 검색하기
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
        parser.add_argument('searchText', location='args')
        args = parser.parse_args()
        auth = kwargs['user']

        userService = UserService()
        result = userService.searchUser(args['searchText'])
        print(userService.searchUser(args['searchText']))
        return make_response(jsonify(result), 200)
