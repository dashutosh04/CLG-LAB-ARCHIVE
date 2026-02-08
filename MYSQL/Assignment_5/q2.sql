--  Find name of the supervisor for employee number 3.
USE corp_emp;

SELECT
    E1.EmployeeId,
    CONCAT (E2.Fname, " ", E2.Lname) AS Employee,
    CONCAT (E1.Fname, " ", E1.Lname) AS Supervisor
FROM
    employee E1,
    employee E2
WHERE
    E2.EmployeeId = 3
    AND E2.Supervisor = E1.EmployeeId;
