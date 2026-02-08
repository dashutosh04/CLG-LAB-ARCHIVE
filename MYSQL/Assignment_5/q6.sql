--  Find all employees in the sales department.
USE corp_emp;

SELECT
    CONCAT (Fname, " ", Lname) AS Name,
    d.DeptName
FROM
    dept AS d
    INNER JOIN employee AS e ON e.EmployeeId = d.EmployeeId
WHERE
    d.DeptName = 'Sales';