-- Display a student’s full name along with his/her major’s description.
USE clg_std;

SELECT
    CONCAT (s.First, " ", s.Last) Name,
    m.MajorDesc
from
    student s
    LEFT JOIN major m ON s.MajorId = m.MajorId;