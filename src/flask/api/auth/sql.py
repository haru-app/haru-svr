class AuthSQL:
    @staticmethod
    def login():
        return """
            SELECT 
                u."userIdx",
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
    def register():
        return """
            INSERT INTO 
                "user"
                (
                    email, 
                    password, 
                    username, 
                    birthday
                )
            VALUES
                (
                    :email, 
                    :password, 
                    :username, 
                    :birthday
                )
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
