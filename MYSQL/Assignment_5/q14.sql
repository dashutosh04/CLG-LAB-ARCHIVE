-- Display course titles along with their prerequisite names. Display courses without prerequisite also.
USE clg_std;

SELECT
    c1.Title AS Course,
    IFNULL (c2.Title, 'No Prerequisite') AS Prerequisite
FROM
    Course c1
    LEFT JOIN Course c2 ON c1.PreReq = c2.CourseId;