from flask_restful import Resource
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
              - name: palette
                in: path
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
        userService = UserService()
        data = userService.getUser();
        return data
