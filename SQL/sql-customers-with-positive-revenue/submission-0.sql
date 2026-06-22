-- Write your query below
-- DESCRIBE customers
-- limit 100;

SELECT
customer_id
FROM customers
WHERE 1=1
AND revenue > 0
AND year = 2020
;