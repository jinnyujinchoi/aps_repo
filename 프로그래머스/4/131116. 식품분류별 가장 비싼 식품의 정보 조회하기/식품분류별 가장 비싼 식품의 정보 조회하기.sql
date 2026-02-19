-- 분류, 가격, 이름 조회 --
SELECT f.CATEGORY,
    f.PRICE as MAX_PRICE,
    f.PRODUCT_NAME
FROM FOOD_PRODUCT f
-- 서브쿼리 조인 --
JOIN (
    SELECT CATEGORY, MAX(PRICE) as MAX_PRICE
    FROM FOOD_PRODUCT
    -- 분류 필터링 --
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY CATEGORY
) m
ON f.CATEGORY = m.CATEGORY
-- 값도 매칭 --
AND f.PRICE = m.MAX_PRICE
-- 내림차 --
ORDER BY MAX_PRICE DESC