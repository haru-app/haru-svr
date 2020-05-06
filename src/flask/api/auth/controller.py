from flask_restful import Resource, reqparse
from .service import UserService


class AuthController(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('test')
        args = parser.parse_args()
        print(args)
        userService = UserService()
        data = userService.getUser();
        return data
