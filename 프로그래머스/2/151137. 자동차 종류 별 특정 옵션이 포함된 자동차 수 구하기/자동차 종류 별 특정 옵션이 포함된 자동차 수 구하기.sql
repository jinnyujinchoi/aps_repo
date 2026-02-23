-- 종류, 몇 대 --
SELECT CAR_TYPE,
    COUNT(*) as CARS
FROM CAR_RENTAL_COMPANY_CAR
-- 옵션 포함(통풍, 열선, 가죽) --
WHERE OPTIONS LIKE '%통풍%'
    OR OPTIONS LIKE '%열선%'
    OR OPTIONS LIKE '%가죽%'
-- 그룹화 --
GROUP BY CAR_TYPE
-- 종류 오름차 --
ORDER BY CAR_TYPE