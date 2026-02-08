-- Which department has more employees than department 1?
use corp_emp;

SELECT
    DeptName
FROM
    dept
WHERE
    DeptId IN (
        SELECT
            DeptId
        FROM
            Employee
        GROUP BY
            DeptId
        HAVING
            COUNT(*) > (
                SELECT
                    COUNT(*)
                FROM
                    Employee
                WHERE
                    DeptId = 1
            )
    );