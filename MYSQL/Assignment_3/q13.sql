-- Display employee’s last name and first name,
-- followed by salary+commission if commission is not null, else display salary only.
USE corp_emp;

SELECT
    CONCAT (Lname, " ", Fname) AS FullName,
    (Salary + (IF (Commission IS NULL, 0, Commission))) AS TotaL
FROM
    employee;