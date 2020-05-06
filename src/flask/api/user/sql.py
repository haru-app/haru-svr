class UserSQL:
    @staticmethod
    def register():
        return """
            INSERT INTO 
                "user" (email, "password", "userName", birthday ) 
            VALUES 
                (:email, :password, :userName, :birthday)
        """
