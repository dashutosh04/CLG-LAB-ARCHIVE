-- Display only the year value from each employee’s hire date.
use corp_emp;

SELECT
    CONCAT (Fname, " ", Lname) AS NAME,
    YEAR (HireDate) AS hire_year
FROM
    employee;