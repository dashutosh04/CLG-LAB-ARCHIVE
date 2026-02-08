-- Display all employees with their commission value. 
-- Display 0 commission foremployees who do not 
-- get any commission.
USE corp_emp;

SELECT
    EmployeeId,
    IFNULL (Commission, 0) AS Commission
FROM
    employee;