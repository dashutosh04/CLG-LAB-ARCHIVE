-- Count the total number of rooms in LOCATION.
USE clg_std;

SELECT
    COUNT(RoomId) AS "Total Rooms"
FROM
    LOCATION;