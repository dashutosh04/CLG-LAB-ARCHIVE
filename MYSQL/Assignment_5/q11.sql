-- Get names of students, who received final grade ‘F’.
USE clg_std;

SELECT
    CONCAT (s.First, " ", s.Last) Name,
    r.final
from
    student s
    LEFT JOIN REGISTRATION r ON s.StudentId = r.StudentId
WHERE
    r.final = 'F';