-- Find the average, highest, and lowest age for students.
USE clg_std;

SELECT
    AVG(TIMESTAMPDIFF (YEAR, birthdate, CURDATE ())) AS "Average Age",
    MAX(TIMESTAMPDIFF (YEAR, birthdate, CURDATE ())) AS "Max Age",
    MIN(TIMESTAMPDIFF (YEAR, birthdate, CURDATE ())) AS "Min Age"
FROM
    student;