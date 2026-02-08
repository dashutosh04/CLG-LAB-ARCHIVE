-- Add more rows to EMP30 table with employee in department 40. Do not transfer employee’s salary.
USE corp_emp;

INSERT INTO
    EMP30 (EmployeeId, Lname, Fname, HireDate)
SELECT
    EmployeeId,
    Lname,
    Fname,
    HireDate
FROM
    Employee
WHERE
    DeptId = 4;