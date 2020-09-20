from src.database import Database
from src.config import Config
from src.flask import FlaskServer

# 설정 파일 불러오기 !
Config()

# Database 엔진 세팅 및 구동
db = Database()
db.start()

flaskServer = FlaskServer()
flaskServer.run()
