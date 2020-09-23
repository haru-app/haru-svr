from src.database.database import Database
from .sql import FriendSQL


class FriendService:
    def getFriendList(self, userIdx):
        result = Database.query(FriendSQL.getFriendList(), {'userIdx': userIdx}).all()
        return result

    def getFriendRequestList(self, userIdx):
        result = Database.query(FriendSQL.getFriendRequestList(), {'userIdx': userIdx}).all()
        return result

    def allowFriendRequest(self, userIdx, friendUserIdx):
        result = Database.query(FriendSQL.allowFriendRequest(), {'userIdx': userIdx, 'friendUserIdx': friendUserIdx})
        return result

    def rejectFriendRequest(self, userIdx, friendUserIdx):
        result = Database.query(FriendSQL.rejectFriendRequest(), {'userIdx': userIdx, 'friendUserIdx': friendUserIdx})
        return result
