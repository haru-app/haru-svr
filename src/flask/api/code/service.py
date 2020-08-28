from src.database.database import Database
from .sql import CodeSQL


class CodeService:
    def getAllCode(self):
        result = Database.query(CodeSQL.getAllCode()).one()
        return result
