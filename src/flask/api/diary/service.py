from src.database.database import Database
from .sql import DiarySQL


class DiaryService:
    def getDiaryList(self, userIdx):
        result = Database.query(DiarySQL.getDiaryList(), {'userIdx': userIdx})
        return result.all()

    def addDiary(self, userIdx, diaryName, diaryIconCode, publicRangeCode):
        def tran(query, commit, rollback):
            resultq = query(DiarySQL.addDiary(),
                            {'userIdx': userIdx, 'diaryName': diaryName, 'diaryIconCode': diaryIconCode,
                             'publicRangeCode': publicRangeCode})
            commit()
            return resultq

        result = Database.transaction(tran)
        return result.all()

    def removeDiary(self, userIdx, diaryIdx):
        result = Database.query(DiarySQL.removeDiary(),
                                {'userIdx': userIdx, 'diaryIdx': diaryIdx})
        return result.all()
