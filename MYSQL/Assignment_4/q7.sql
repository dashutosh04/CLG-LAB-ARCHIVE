-- Write a query to find the date of the last Sunday of the current month.
SELECT
    DATE_SUB (
        LAST_DAY (SYSDATE ()),
        INTERVAL (DAYOFWEEK (LAST_DAY (SYSDATE ())) - 1) DAY
    ) AS FinalSunday;