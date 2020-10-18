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
