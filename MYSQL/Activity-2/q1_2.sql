-- Find the dept details where contact is missing.
SELECT
    *
FROM
    dept
WHERE
    contact is NULL;