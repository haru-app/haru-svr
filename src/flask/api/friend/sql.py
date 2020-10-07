class FriendSQL:
    @staticmethod
    def getFriendList():
        return """
        SELECT
            u.username, u."userIdx"
        FROM
            friend f
        INNER JOIN friend f2 ON
            f2."friendUserIdx" = f."userIdx" AND
            f2."userIdx" = f."friendUserIdx" 
        INNER JOIN "user" u ON
          u."userIdx" = f."friendUserIdx" 
        WHERE
            f."userIdx" = :userIdx
        """

    @staticmethod
    def getFriendRequestList():
        return """
        SELECT 
	        u."userIdx", u.username
        FROM 
	        friend f
        LEFT OUTER JOIN friend f2 ON
	        f2."friendUserIdx" = f."userIdx"
        INNER JOIN "user" u ON
	        u."userIdx" = f."userIdx" 
        WHERE
	        f."friendUserIdx" = :userIdx AND
	        f2."userIdx" IS NULL 
        """

    @staticmethod
    def allowFriendRequest():
        return """
            INSERT INTO 
                friend
                (
                    "userIdx",
                    "friendUserIdx" 
                )
            VALUES 
                (
                    :userIdx,
                    :friendUserIdx
                ) 
        """

    @staticmethod
    def rejectFriendRequest():
        return """
        DELETE
        FROM
	        friend
        WHERE
	        "userIdx" = :userIdx
	        AND "friendUserIdx" = :friendUserIdx
        """

    @staticmethod
    def checkFriend():
        return """
        SELECT
            f."userIdx" as userIdx , f."friendUserIdx" as friendUserIdx , f2."userIdx" as userIdx2, f2."friendUserIdx" as friendUserIdx2
        FROM 
            friend f
        FULL OUTER JOIN friend f2 ON 
            f."userIdx" = f2."friendUserIdx" AND
            f."friendUserIdx" = f2."userIdx" 
        WHERE
            (f."userIdx" = :userIdx AND f."friendUserIdx" = :friendUserIdx)
            OR (f2."userIdx" = :friendUserIdx AND f2."friendUserIdx" = :userIdx)
        """

    @staticmethod
    def deleteFriend():
        return """
        DELETE
        FROM
	        friend
        WHERE
	        "userIdx" in (:userIdx, :friendUserIdx)
	        AND "friendUserIdx" in (:friendUserIdx, :userIdx)
        """
