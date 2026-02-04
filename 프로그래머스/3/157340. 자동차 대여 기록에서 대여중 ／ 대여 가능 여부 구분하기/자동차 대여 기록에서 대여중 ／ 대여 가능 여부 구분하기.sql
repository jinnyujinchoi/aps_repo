SELECT CAR_ID,
    -- 존재 여부 1,0으로 나누기 --
    CASE
        WHEN MAX(
            -- 2022/10/16 -> 대여중 --
            CASE
                WHEN START_DATE <= '2022-10-16'
                AND END_DATE >= '2022-10-16'
                THEN 1 ELSE 0
            END
        ) = 1
        THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC