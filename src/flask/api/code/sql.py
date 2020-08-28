class CodeSQL:
    @staticmethod
    def getAllCode():
        return """
            WITH o AS (
                SELECT
                    ct."codeType",
                    jsonb_object_agg(ct.code, ct."name") AS code
                FROM 
                    "code" ct
                GROUP BY
                    ct."codeType"
            ),
            a AS (
                SELECT
                    ct."codeType",
                    jsonb_agg(jsonb_build_object('code', ct.code, 'name', ct."name") ORDER BY ct.sort ASC) AS code
                FROM 
                    "code" ct
                GROUP BY
                    ct."codeType"
            )
            SELECT
                jsonb_object_agg(o."codeType", o.code) AS "object",
                jsonb_object_agg(a."codeType", a.code) AS "array"
            FROM
                o, a
        """
