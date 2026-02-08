-- Display each employee’s name, department name, 
-- position description, and qualification description. 
-- Which employee is missing? Why?
USE corp_emp;

SELECT
    CONCAT (e.Fname, " ", e.Lname) AS Name,
    d.DeptName,
    p.PosDesc,
    q.QualDesc
FROM
    employee AS e
    CROSS JOIN dept as d ON e.DeptId = d.DeptId
    CROSS JOIN position as p ON p.PositionId = e.PositionId
    CROSS JOIN qualification as q ON e.QualId = q.QualId;

SELECT
    e.EmployeeId,
    CONCAT (e.Fname, " ", e.Lname) AS Missing_Employee
FROM
    employee e
    LEFT JOIN dept d ON e.DeptId = d.DeptId
    LEFT JOIN position p ON e.PositionId = p.PositionId
    LEFT JOIN qualification q ON e.QualId = q.QualId
WHERE
    d.DeptId IS NULL
    OR p.PositionId IS NULL
    OR q.QualId IS NULL
UNION
SELECT
    e.EmployeeId,
    CONCAT (e.Fname, " ", e.Lname) AS Name
FROM
    employee e
    RIGHT JOIN dept d ON e.DeptId = d.DeptId
    RIGHT JOIN position p ON e.PositionId = p.PositionId
    RIGHT JOIN qualification q ON e.QualId = q.QualId
WHERE
    e.EmployeeId IS NULL;