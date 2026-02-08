-- Display all student names and birth dates. 
-- Display birth dates with the format ‘20 OCTOBER, 1970’.
USE clg_std;

SELECT
    CONCAT (First, " ", Last) AS NAME,
    DATE_FORMAT (BirthDate, '%d %M, %Y') AS Birthday
FROM
    student;