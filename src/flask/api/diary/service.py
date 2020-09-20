from src.database.database import Database
from .sql import DiarySQL


class DiaryService:
    def getDiaryList(self, userIdx):
        result = Database.query(DiarySQL.getDiaryList(), {'userIdx': userIdx})
        return result.all()
