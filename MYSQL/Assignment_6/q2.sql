--  Find name of the supervisor for employee number 3.
USE corp_emp;

SELECT
    CONCAT (Fname, " ", Lname) Name
FROM
    Employee
WHERE
    EmployeeId = (
        SELECT
            Supervisor
        FROM
            Employee
        WHERE
            EmployeeId = 3
    );