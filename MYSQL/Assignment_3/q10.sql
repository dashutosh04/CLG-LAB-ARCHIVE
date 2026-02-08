-- Display courses and prerequisites. 
-- If there is no prerequisite, display ‘none’ else display ‘one’.
USE clg_std;

SELECT
    CourseId,
    IF (PreReq IS NULL, 'none', 'one') AS prerequisite
FROM
    course;