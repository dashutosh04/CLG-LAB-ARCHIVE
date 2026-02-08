-- Write a subquery that finds average salary by each department. 
-- Check to find if employee 543’s salary satisfies =ANY, <ANY, >ANY, <ALL, or >ALL condition against those departmental average salaries.
use corp_emp;

SELECT
    *
FROM
    Employee
WHERE
    EmployeeId = 3
    AND Salary < ALL (
        SELECT
            AVG(Salary)
        FROM
            Employee
        GROUP BY
            DeptId
    );