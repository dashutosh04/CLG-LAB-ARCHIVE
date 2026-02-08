-- Find employees with minimum salary in their own department with the use of correlated subquery.
USE corp_emp;

SELECT
    Fname,
    Lname,
    DeptId,
    Salary
FROM
    Employee E1
WHERE
    Salary = (
        SELECT
            MIN(Salary)
        FROM
            Employee E2
        WHERE
            E2.DeptId = E1.DeptId
    );