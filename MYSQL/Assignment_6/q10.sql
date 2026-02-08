-- Use multiple level subquery to display dependent information for employees, who belong to FINANCE department.
USE corp_emp;

SELECT
    *
FROM
    dependent
WHERE
    EmployeeId IN (
        SELECT
            EmployeeId
        FROM
            employee
        WHERE
            DeptId IN (
                SELECT
                    DeptId
                FROM
                    dept
                WHERE
                    DeptName = 'Sales'
            )
    );