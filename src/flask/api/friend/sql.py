class FriendSQL:
    @staticmethod
    def getFriendList():
        return """
        SELECT
            u.username 
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
