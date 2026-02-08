-- Display employee Vivek Sharma’s department name.
USE corp_emp;

SELECT
    DeptName
FROM
    dept
WHERE
    DeptId = (
        SELECT
            DeptId
        FROM
            Employee
        WHERE
            Fname = 'Vivek'
            AND Lname = 'Sharma'
    );