import decimal
from flask import Flask, jsonify, make_response
from flask.json import JSONEncoder
from flask_restful import Api
from flasgger import Swagger
from datetime import date

from werkzeug.exceptions import InternalServerError, HTTPException

from .api import Api as MyApi

# 웹 서버 구동
from src.utils.customError import CustomError

"""
401 인증오류
403 쿠키는 있으나 권한이 없음 (마스터인지 유저인지)
404 페이지 없음
422 파라미터, 바디 오류

500 서버 오류
"""


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        return JSONEncoder.default(self, obj)


class FlaskServer:
    app = None
    swagger = None

    def __init__(self):
        appVar = self.app = Flask(__name__)

        self.app.config['JSON_AS_ASCII'] = False

        @appVar.errorhandler(Exception)
        def all_exception(error):
            if isinstance(error, CustomError):
                print('-----------E R R O R-----------')
                print(error.get())
                print('-----------E R R O R-----------')
                return make_response(jsonify(error.get()), error.status)
            print('-----------E R R O R-----------')
            print(error)
            print('-----------E R R O R-----------')
            return CustomError().get(), 500

        self.app.json_encoder = MyJSONEncoder
        swagger_config = {
            "headers": [],
            "openapi": "3.0.2",
            "components": {
                "securitySchemes": {
                    "oAuthSample": {
                        "type": "oauth2",
                        "flows": {
                            "clientCredentials": {
                                "tokenUrl": "https://api.pgsmartshopassistant.com/o/token/",
                            }
                        }
                    }
                },
            },
            "servers": [
                {
                    "url": "https://api.example.com/v1",
                    "description": "Production server (uses live data)"
                },
                {
                    "url": "https://sandbox-api.example.com:8443/v1",
                    "description": "Sandbox server (uses test data)"
                }
            ],
            "specs": [
                {
                    "endpoint": "swagger",
                    "route": "/api/swagger.json",
                    "rule_filter": lambda rule: True,
                    "model_filter": lambda tag: True,
                }
            ],
            "title": "Haru API",
            "version": '1.0.0',
            "termsOfService": "https://www.naver.com",
            "static_url_path": "/api/swagger/static",
            "swagger_ui": True,
            "specs_route": "/api/swagger/",
            "description": "Haru API Documentation",
        }
        self.swagger = Swagger(self.app, config=swagger_config)
        self.api = Api(self.app)
        self.initRouter()

    def initRouter(self):
        routers = MyApi().getRouters()
        for r in routers:
            self.api.add_resource(r['class'], r['path'])

    def run(self):
        self.app.run(host='0.0.0.0', debug=True)
