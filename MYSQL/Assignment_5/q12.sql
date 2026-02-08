-- Display student names, their faculty advisors names, and faculty’s office location.
USE clg_std;

SELECT
    CONCAT (s.First, " ", s.Last) Name,
    f.name Faculty_Name,
    l.RoomNo
FROM
    student s
    LEFT JOIN faculty f ON s.Facultyid = f.Facultyid
    LEFT JOIN location l ON l.RoomId = f.RoomId;