-- Find the employees of CSE dept;
SELECT
    e.id, e.ename,e.sal,e.age,e.doj
FROM
    Emp e
    JOIN Dept D ON e.