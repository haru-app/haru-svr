from src.database.database import Database
from .sql import UserSQL


class UserService:
    def duplicateEmail(self, email):
        result = Database.query(UserSQL.getDuplicateEmail(),
                                {'email': email}).one()
        return result

    def searchUser(self, searchText, userIdx):
        result = Database.query(UserSQL.getSearchUserList(), {'searchText': searchText, 'userIdx': userIdx}).all()
        return result

    def sendNotice(self, userIdx, noticeTypeCode, noticeData, isCheck):
        result = Database.query(UserSQL.sendNotice(),
                                {'userIdx': userIdx, 'noticeTypeCode': noticeTypeCode, 'noticeData': noticeData,
                                 'isCheck': isCheck})
        return result
