-- Find average employee commission.
-- Ignore nulls.
-- Do not ignore nulls.
USE corp_emp;

SELECT
    AVG(Commission) AS average_commission
FROM
    employee;

SELECT
    AVG(IFNULL (Commission, 0)) AS avg_comm
FROM
    employee;