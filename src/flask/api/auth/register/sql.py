class RegisterSQL:
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
