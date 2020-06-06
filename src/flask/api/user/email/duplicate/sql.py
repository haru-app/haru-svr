class DuplicateEmailSQL:
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
