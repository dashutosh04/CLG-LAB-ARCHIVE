-- Get Winter 2020 course sections with the faculty member assigned to teach the class. 
-- Include course sections without any faculty assigned to them.
use clg_std;

SELECT
    c.TermId,
    c.FacultyId,
    f.Name
FROM
    crssection c
    INNER JOIN faculty f ON f.FacultyId = c.FacultyId
WHERE
    c.TermId = 'Winter 2020';