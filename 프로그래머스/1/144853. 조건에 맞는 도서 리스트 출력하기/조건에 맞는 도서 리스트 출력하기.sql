-- 코드를 입력하세요
select BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d")AS PUBLISHED_DATE from BOOK
WHERE (PUBLISHED_DATE BETWEEN '2021-01-01' AND '2021-12-31') AND CATEGORY = "인문"
ORDER BY PUBLISHED_DATE
