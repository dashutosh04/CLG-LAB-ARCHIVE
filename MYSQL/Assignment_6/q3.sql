-- Who has same qualification as Vivek Sharma?
use corp_emp;

SELECT
    CONCAT (Fname, " ", Lname) AS Name
FROM
    Employee
WHERE
    QualId IN (
        SELECT
            QualId
        FROM
            Employee
        WHERE
            Fname = 'Vivek'
            AND Lname = 'Sharma'
    );

SELECT
    *
FROM
    employee;