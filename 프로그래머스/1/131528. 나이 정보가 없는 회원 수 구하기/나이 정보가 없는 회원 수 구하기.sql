-- 코드를 입력하세요
SELECT SUM(CASE WHEN age IS NULL THEN 1 END) as USERS from USER_INFO