-- INSERT a new Winter 2004 term in the TERM table. Use a SELECT query to see the result. 
-- Ask the user XYZ with the SELECT privilege to view your TERM table. 
-- COMMIT your transaction and ask the same user to view the table again.
USE clg_std;

INSERT INTO
    TERM (TermId, TermDesc, StartDate, EndDate)
VALUES
    (7, 'Winter 2004', '2004-01-01', '2004-03-31');

SELECT
    *
FROM
    TERM;