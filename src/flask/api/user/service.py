from src.database.database import Database
from .sql import UserSQL


class UserService:
    def duplicateEmail(self, email):
        result = Database.query(UserSQL.getDuplicateEmail(),
                                {'email': email}).one()
        return result

    def searchUser(self, searchText):
        result = Database.query(UserSQL.getSearchUserList(), {'searchText': searchText}).all()
        return result
