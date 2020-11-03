class UserSQL:
    @staticmethod
    def getDuplicateEmail():
        return """
            SELECT 
                CASE WHEN COUNT(*) > 0 THEN TRUE ELSE FALSE END AS "isDuplicateEmail"
            FROM 
                "user" u
            WHERE
                u.email = :email
        """

    @staticmethod
    def getSearchUserList():
        return """
            SELECT
                u."userIdx", u.email, u.username
            FROM 
                "user" u
            WHERE 
                ( u.username LIKE :searchText || '%' OR
                u.email LIKE :searchText || '%' ) AND 
                u."userIdx" != :userIdx
        """

    @staticmethod
    def sendNotice():
        return """
            INSERT INTO 
                "notice" 
                (
	                "userIdx",
	                "noticeTypeCode" ,
	                "noticeData" ,
	                "isCheck" 
                )
            VALUES 
                (
	                :userIdx,
	                :noticeTypeCode,
	                :noticeData,
	                :isCheck	
                )
        """
