-- Which employees are working in the company longer than Vivek Sharma?
use corp_emp;

SELECT
    Fname,
    Lname,
    HireDate
FROM
    Employee
WHERE
    HireDate < (
        SELECT
            HireDate
        FROM
            Employee
        WHERE
            Fname = 'Raj'
            AND Lname = 'Kumar'
    );