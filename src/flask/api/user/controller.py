from flask_restful import Resource, reqparse
from .service import UserService


class UserController(Resource):
    def get(self):
        """
            Example endpoint returning a list of colors by palette
            This is using docstrings for specifications.
            ---
            tags:
              - calllbacks
            parameters:
              - name: test
                in: query
                schema:
                  type: string
                  enum: ['all', 'rgb', 'cmyk']
                required: true
                default: all
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
        parser.add_argument('test')
        args = parser.parse_args()
        print(args)
        userService = UserService()
        data = userService.getUser();
        return data
