-- Find the number of years employees have been working for. Display integer part of value only.
USE corp_emp;

SELECT
    CONCAT (Fname, " ", Lname) AS NAME,
    TIMESTAMPDIFF (YEAR, HireDate, CURDATE ()) AS years_worked
FROM
    employee;