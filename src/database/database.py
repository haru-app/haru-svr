from sqlalchemy import create_engine, text, exc
import decimal
from src.config import Config


class Database:
    engine = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super().__init__()

    def start(self):
        if self.engine is not None:
            return

        dbConfig = Config.getConfig()['database']
        db_path = "postgres+psycopg2://{}:{}@{}:{}/{}".format(dbConfig['user'], dbConfig['password'],
                                                              dbConfig['host'], dbConfig['port'], dbConfig['database'])
        Database.engine = create_engine(db_path, encoding='utf-8', pool_size=10, max_overflow=0)

    @staticmethod
    def query(sql, *parameters):
        if Database is None:
            raise Exception("DB 엔진이 시작되지 않았습니다.")
        data = None
        count = None
        with Database.engine.connect() as conn:
            result = conn.execute(text(sql), parameters)
            count = result.rowcount
            try:
                data = result.fetchall()
            except exc.ResourceClosedError:
                data = None
        return ResultData({'rowCount': count, 'data': data})


class ResultData:
    allData = None
    rowCount = None
    dictAllData = None

    def __init__(self, result):
        self.allData = result['data']
        self.rowCount = result['rowCount']
        if self.allData is not None:
            self.dictAllData = [dict(r) for r in self.allData]

    def one(self):
        return self.dictAllData[0] if len(self.dictAllData) > 0 else None

    def all(self):
        return self.dictAllData

    def count(self):
        return self.count

    def scalar(self):
        return self.allData[0] if len(self.allData) > 0 and (
                isinstance(self.allData[0][0], int) or isinstance(self.allData[0][0], float) or
                isinstance(self.allData[0][0], decimal.Decimal)) else None
