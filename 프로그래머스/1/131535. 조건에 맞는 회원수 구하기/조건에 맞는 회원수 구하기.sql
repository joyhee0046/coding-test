-- 코드를 입력하세요
-- SELECT AGE from USER_INFO


-- select SUM(CASE WHEN (20 <= AGE , AGE <= 29 , AGE is not null) THEN 1 END) as USERS from USER_INFO

select count(case when age >=20 and age<=29 then USER_ID end) as USERS from USER_INFO
WHERE JOINED BETWEEN '2021-01-01' AND '2021-12-31'