from src.database.database import Database
from .sql import WritingSQL


class WritingService:
    def __init__(self, user):
        self.user = user

    def addWriting(self, diaryIdx, writingDate, title, content, score, writingTags):
        def transFunc(query, commit, rollback):
            result = query(WritingSQL.addWriting(),
                           {'diaryIdx': diaryIdx, 'writingDate': writingDate, 'userIdx': self.user['userIdx'],
                            'title': title,
                            'content': content, 'score': score})

            if len(writingTags) > 0:
                query(WritingSQL.addWritingTag(),
                      {'writingIdx': result.one()['writingIdx'], 'writingTags': writingTags})
            commit()

        Database.transaction(transFunc)

    def getWriting(self, diaryIdx):
        result = Database.query(WritingSQL.getWritingList(), {'diaryIdx': diaryIdx, 'userIdx': self.user['userIdx']})

        return result.all()
