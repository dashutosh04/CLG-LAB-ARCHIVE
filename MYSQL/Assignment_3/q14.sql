-- Display employee’s full name followed by a message based on salary. 
-- If salary is above ₹60,000, display “HIGH”.
-- If salary is between ₹50,000 and ₹60,000, display “MEDIUM”. 
-- If salary is below ₹50,000, display “LOW”.
USE corp_emp;

SELECT
    CONCAT (Fname, " ", Lname) AS Full_Name,
    IF (
        salary >= 60000,
        "HIGH",
        IF (salary <= 50000, "LOW", "MEDIUM")
    ) AS message
FROM
    employee;