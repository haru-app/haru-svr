from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from .service import UserService
from src.flask.decorator.auth import AuthDecorator


class UserController(Resource):
    method_decorators = {'post': [AuthDecorator.decorator]}

    def post(self):
        """
            회원가입을 합니다.
            ---
            tags:
                - user
            requestBody:
                description: Optional description in *Markdown*
                required: true
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                email:
                                    type: string
                                password:
                                    type: string
                                userName:
                                    type: string
                                birthday:
                                    type: string
                            required:
                                - email
                                - password
                                - userName
            definitions:
                Palette:
                    type: object
                    properties:
                    palette_name:
                        type: array
                        items:
                            $ref: '#/definitions/Color'
                Color:
                    type: string
            responses:
                200:
                    description: A list of colors (may be filtered by palette)
                    schema:
                    $ref: '#/definitions/Palette'
                    examples:
                    rgb: ['red', 'green', 'blue']
        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, type=str)
        parser.add_argument('password', required=True, type=str)
        parser.add_argument('userName', required=True, type=str)
        parser.add_argument('birthday', required=False, default=None, type=str)
        args = parser.parse_args()

        userService = UserService()
        userService.register(args)
        return make_response(jsonify(), 200)
