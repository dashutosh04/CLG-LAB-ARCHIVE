-- Find out the names and number of years worked along with their
-- department names in descending order by number of years worked.
USE corp_emp;

SELECT
    CONCAT (e.Fname, " ", e.LName) AS Name,
    TIMESTAMPDIFF (YEAR, e.HireDate, CURDATE ()) Year_Worked,
    d.DeptName
FROM
    employee AS e
    INNER JOIN dept AS d ON d.DeptId = e.DeptId
ORDER BY
    Year_Worked DESC;