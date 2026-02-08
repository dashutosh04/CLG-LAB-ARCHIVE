-- Find sum of Maximum count by term and course. (GROUP BY two columns)
USE clg_std;

SELECT
    SUM(max_count) AS total_max
FROM
    (
        SELECT
            TermId,
            CourseId,
            COUNT(*) AS max_count
        FROM
            crssection
        GROUP BY
            TermId,
            CourseId
    ) AS grouped_counts;