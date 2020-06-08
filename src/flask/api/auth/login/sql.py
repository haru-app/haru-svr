class LoginSQL:
    @staticmethod
    def login():
        return """
            SELECT 
                u.email,
                u."username"
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

    @staticmethod
    def updateUpdateTime():
        return """
            UPDATE 
                "user" u
            SET
                "updateTime" = now()
            WHERE 
                u.email = :email
        """
