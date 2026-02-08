-- Find all employees in the sales department by using a nested query.
use corp_emp;

SELECT
    Fname,
    Lname,
    DeptId
FROM
    Employee
WHERE
    DeptId = (
        SELECT
            DeptId
        FROM
            Dept
        WHERE
            DeptName = 'SALES'
    );