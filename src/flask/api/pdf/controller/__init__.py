from flask_restful import Resource, reqparse
from flask import jsonify, make_response, send_file
from src.flask.api.friend.service import FriendService
from src.flask.decorator.auth import AuthDecorator


class PdfController(Resource):

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
        print('test')
        return send_file('./api/pdf/sample.pdf', as_attachment=True)
