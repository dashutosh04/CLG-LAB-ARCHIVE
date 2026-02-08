-- Count number of faculty members in each department.
USE clg_std;

SELECT
    COUNT(*) AS faculty_count
FROM
    faculty
GROUP BY
    FacultyId;