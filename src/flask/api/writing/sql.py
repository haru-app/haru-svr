class WritingSQL:
    @staticmethod
    def addWriting():
        return """
        INSERT INTO 
            "diaryWriting" (
                "diaryIdx",
                "userIdx",
                "writingDate",
                title,
                "content",
                score
            )
        VALUES (
            :diaryIdx,
            :userIdx,
            :writingDate,
            :title,
            :content,
            :score
        )
        RETURNING
            "writingIdx"
        """

    @staticmethod
    def addWritingTag():
        return """
        WITH datas AS (
            SELECT UNNEST(:writingTags) AS "hashTagName"
        ),
        hash AS (
            INSERT INTO 
                "hashTag" (
                    "hashTagName" 
                )
            SELECT
                "hashTagName" 
            FROM
                datas
            RETURNING
                "hashTagIdx"
        )
        INSERT INTO
            "writingTag" (
                "writingIdx",
                "hashTagIdx"
            )
        SELECT
            (:writingIdx)::int,
            "hashTagIdx"
        FROM 
            hash 
        """

    @staticmethod
    def getWritingList():
        return """
        SELECT
            dw.title,
            dw."content",
            dw.score,
            dw."writingDate",
            CASE WHEN jsonb_agg(ht."hashTagName") ->> 0 IS NULL THEN '[]'::jsonb ELSE jsonb_agg(ht."hashTagName") END
        FROM
            "diaryWriting" dw 
        LEFT OUTER JOIN "writingTag" wt ON
            wt."writingIdx" = dw."writingIdx"
        LEFT OUTER JOIN "hashTag" ht ON
            ht."hashTagIdx" = wt."hashTagIdx"
        INNER JOIN "diaryMember" dm ON
            dm."diaryIdx" = dw."diaryIdx" AND
            dm."userIdx" = :userIdx
        WHERE
            dw."diaryIdx" = :diaryIdx
        GROUP BY
            dw.title,
            dw."content",
            dw.score,
            dw."writingDate"
        """
