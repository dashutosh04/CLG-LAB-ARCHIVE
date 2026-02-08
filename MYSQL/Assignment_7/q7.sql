-- 7. Input a number and print its multiplication table using a WHILE loop.
use clg_std;

DROP PROCEDURE IF EXISTS multiplication_table;

CREATE PROCEDURE multiplication_table() 
BEGIN DECLARE num INT DEFAULT 5;

DECLARE i INT DEFAULT 1;

DECLARE result INT;

WHILE i <= 10 DO
SET
    result = num * i;

SELECT
    CONCAT (num, ' x ', i, ' = ', result) AS Multiplication;

SET
    i = i + 1;

END WHILE;

END;

CALL multiplication_table ();