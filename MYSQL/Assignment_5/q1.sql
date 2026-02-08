-- 1. Display all employee names and their department names.
USE corp_emp;

SELECT
    CONCAT (e.Fname, " ", e.Lname) AS Name,
    d.DeptName
FROM
    employee AS e
    INNER JOIN dept as d ON e.DeptId = d.DeptId;