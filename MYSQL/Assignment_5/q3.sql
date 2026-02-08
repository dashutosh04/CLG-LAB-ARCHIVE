--  Find all employees’ full names (lastname, firstname format) with salary, and their supervisor’s name with salary.
USE corp_emp;

SELECT
    CONCAT (E2.Fname, " ", E2.Lname) AS Employee,
    E2.Salary AS Employee_Salary,
    CONCAT (E1.Fname, " ", E1.Lname) AS Supervisor,
    E1.Salary AS Supervisor_Salary
FROM
    employee E1,
    employee E2
WHERE
    E2.Supervisor = E1.EmployeeId;