-- Display employee names and dependent information using an outer join.
use corp_emp;

SELECT
    CONCAT (e.Fname, " ", e.LName) AS Name,
    d.*
FROM
    employee as e
    LEFT JOIN dependent AS d ON e.EmployeeId = d.EmployeeId
UNION
SELECT
    CONCAT (e.Fname, " ", e.LName) AS Name,
    d.*
FROM
    employee as e
    RIGHT JOIN dependent AS d ON e.EmployeeId = d.EmployeeId;