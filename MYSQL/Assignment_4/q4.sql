-- Display average employee salary by department, but do not include departments with average salary less than ₹50000.
USE corp_emp;

SELECT
    DeptId,
    AVG(Salary) AS average_salary
FROM
    employee
GROUP BY
    DeptId
HAVING
    AVG(salary) >= 50000;