from datetime import datetime
from dateutil import parser

import cerberus

from src.utils.customError import CustomError


class CustomValidator(cerberus.Validator):
    def __init__(self, *args, **kwargs):
        super(CustomValidator, self).__init__(*args, **kwargs)

    def _normalize_coerce_utcDatetime(self, value):
        return parser.parse(value)


class Validator:
    @staticmethod
    def validate(schema, value):
        v = CustomValidator(schema)
        result = v.validate(value)
        if not result:
            print(v.errors)
            raise CustomError(422, 1000, '잘 못 입력한 값이 있습니다.', [*v.errors])
        return v.normalized(value)

    @staticmethod
    def email(options={}):
        return dict({'type': 'string', 'regex': r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', 'coerce': str},
                    **options)

    @staticmethod
    def password(options={}):
        return dict({'type': 'string', 'regex': r'^(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9])(?=.*[0-9]).{8,16}$', 'coerce': str},
                    **options)

    @staticmethod
    def username(options={}):
        return dict({'type': 'string', 'regex': r'[가-힣]{2,8}|[a-zA-Z]{4,16}', 'coerce': str}, **options)

    @staticmethod
    def birthday(options={}):
        return dict({'type': 'datetime', 'coerce': 'utcDatetime'}, **options)
