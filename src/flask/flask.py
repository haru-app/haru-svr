import decimal
from flask import Flask, jsonify
from flask.json import JSONEncoder
from flask_restful import Resource, Api
from flasgger import Swagger
from datetime import datetime, date
from src.database.database import Database


# 웹 서버 구동
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
        self.app = Flask(__name__)
        self.app.json_encoder = MyJSONEncoder
        self.app.config['SWAGGER'] = {
            'title': 'Haru API',
            'openapi': '3.0.2'
        }
        self.swagger = Swagger(self.app)
        self.api = Api(self.app)
        self.initRouter()

    def initRouter(self):
        self.api.add_resource(HelloWorld, '/asd')

    def run(self):
        self.app.run(debug=True)


class HelloWorld(Resource):
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
        data = Database.query('SELECT * FROM "testTable"').all()
        print(datetime.now())
        test = dict({'time': datetime.now()})
        return jsonify(test)
