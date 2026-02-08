-- Create a new table, EMP30, and populate it with employees in department 30, using an existing table and a subquery. 
-- Use EmployeeId, Lname, Fname,HireDate and Salary columns.
USE corp_emp;

CREATE TABLE
    EMP30 AS
SELECT
    EmployeeId,
    Lname,
    Fname,
    HireDate,
    Salary
FROM
    Employee
WHERE
    DeptId = 3;