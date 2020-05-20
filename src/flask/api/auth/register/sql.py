class RegisterSQL:
    @staticmethod
    def login():
        return """
            SELECT 
                u."userIdx",
                u.email,
                u."userName",
                u."createTime",
                u."updateTime"
            FROM 
                "user" u 
            WHERE 
                u.email = :email AND
                u."password" = :password
        """

    @staticmethod
    def updateRefreshToken():
        return """
            UPDATE 
                "user" u
            SET
                "refreshToken" = :refreshToken
            WHERE 
                u.email = :email
        """
