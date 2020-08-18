from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request

from src.flask.api.auth.service import AuthService


class TokenController(Resource):
    def put(self, *args, **kwargs):
        """
            토큰
            ---
            description: 토큰 업데이트를 합니다.
            tags:
              - auth
            requestBody:
              description: 로그인 내용
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - accessToeken
                      - refreshToken
                    properties:
                      accessToeken:
                        description: 액세스 토큰
                        type: string
                      refreshToken:
                        description: 리프레쉬 토큰
                        type: string
            responses:
              200:
                description: 성공
              500:
                description: 실패
        """
        print(request.data);
        parser = reqparse.RequestParser()
        parser.add_argument('accessToken', location='json')
        parser.add_argument('refreshToken', location='json')
        args = parser.parse_args()

        authService = AuthService()
        data = authService.updateToken(args['accessToken'], args['refreshToken'])
        return make_response(data, 200)
