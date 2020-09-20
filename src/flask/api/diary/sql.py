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
