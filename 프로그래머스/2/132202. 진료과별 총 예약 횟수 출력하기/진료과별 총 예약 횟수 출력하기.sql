-- 코드, 환자 예약 수 --
SELECT MCDP_CD as '진료과코드',
    COUNT(DISTINCT PT_NO) as '5월예약건수'
FROM APPOINTMENT
-- 2022년 5월 예약 --
WHERE APNT_YMD >= '2022-05-01'
    AND APNT_YMD < '2022-06-01'
-- 코드 별로 --
GROUP BY MCDP_CD
-- 환자 수 오름차, 코드 오름차 --
ORDER BY 2, 1

