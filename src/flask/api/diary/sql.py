class DiarySQL:
    @staticmethod
    def getDiaryList():
        return """
            SELECT
                d."diaryIdx",
                d."userIdx",
                d."diaryName",
                d."diaryIconCode",
                d."publicRangeCode" 
            FROM
                diary d
            WHERE
                d."userIdx" = :userIdx
            ORDER BY d."createTime" 
        """

    @staticmethod
    def addDiary():
        return """
            WITH diary AS (
                INSERT INTO
                    diary (
                        "userIdx",
                        "diaryName",
                        "diaryIconCode",
                        "publicRangeCode"
                    )
                VALUES (
                    :userIdx,
                    :diaryName,
                    :diaryIconCode,
                    :publicRangeCode
                )
                RETURNING
                    "diaryIdx"
            )
            INSERT INTO
                "diaryMember" (
                    "diaryIdx",
                    "userIdx",
                    "isAccept"
                )
            SELECT
                "diaryIdx",
                (:userIdx)::int,
                TRUE
            FROM
                diary
            RETURNING
                "diaryIdx"
        """

    @staticmethod
    def removeDiary():
        return """
        DELETE FROM
            diary 
        WHERE
            "diaryIdx" = :diaryIdx AND
            "userIdx" = :userIdx
        """
