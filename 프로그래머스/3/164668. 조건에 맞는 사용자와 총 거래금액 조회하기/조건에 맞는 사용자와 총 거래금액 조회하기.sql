-- 회원ID, 닉네임, 총거래금액 조회 --
SELECT ugu.USER_ID,
    ugu.NICKNAME,
    SUM(ugb.PRICE) as TOTAL_SALES
FROM USED_GOODS_BOARD ugb
-- 조인 --
JOIN USED_GOODS_USER ugu
ON ugb.WRITER_ID = ugu.USER_ID
-- 거래상태: 완료 --
WHERE ugb.STATUS = 'DONE'
-- 그룹화 --
GROUP BY ugu.USER_ID
-- 가격: 70만 이상 --
HAVING TOTAL_SALES >= 700000
-- 거래금액 오름차 --
ORDER BY TOTAL_SALES