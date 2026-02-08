-- Count the distinct building names in LOCATION.
USE clg_std;

SELECT
    COUNT(distinct (Building)) AS Buildings
FROM
    LOCATION;