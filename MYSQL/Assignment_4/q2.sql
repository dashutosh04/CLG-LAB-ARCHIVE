-- Display the total number of dependents for each employee.
USE corp_emp;

SELECT
    EmployeeId,
    COUNT(*) AS dependents
from
    DEPENDENT
GROUP BY
    EmployeeId;