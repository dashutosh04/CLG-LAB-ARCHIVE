-- Find students who are born in the month of May.
USE clg_std;

SELECT
    StudentId,
    CONCAT (First, " ", Last) AS Name
FROM
    student
WHERE
    MONTH (BirthDate) = 5;