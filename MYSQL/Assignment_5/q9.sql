-- Who works in the same department in which Raj Kumar works?
USE corp_emp;

SELECT
    CONCAT (e1.Fname, " ", e1.Lname) AS Name
FROM
    employee e1,
    employee e2
WHERE
    e2.Fname = 'Raj'
    AND e1.DeptId = e2.DeptId;