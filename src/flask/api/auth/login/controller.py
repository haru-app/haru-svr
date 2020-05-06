from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from .service import LoginService


class LoginController(Resource):
    def get(self):
        """
            로그인을 합니다.
            ---
            tags:
              - auth
            parameters:
              - name: email
                in: query
                schema:
                  type: string
                required: true
              - name: password
                in: query
                schema:
                  type: string
                required: true
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
        args = parser.parse_args()
        loginService = LoginService()
        data = loginService.login(args['email'], args['password'])
        return make_response(jsonify(data), 200)
