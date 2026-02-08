-- 3. Write a PL/SQL block to swap the values of two variables. Print variables before and after swapping.
use clg_std;

DROP PROCEDURE IF EXISTS swap_variables;

CREATE PROCEDURE swap_variables()
BEGIN 
    DECLARE a INT DEFAULT 10;
    DECLARE b INT DEFAULT 20;
    DECLARE temp INT;
    SELECT
        CONCAT ('Before swapping: a = ', a, ', b = ', b) AS BeforeSwap;

    SET
        temp = a;
    SET
        a = b;
    SET
        b = temp;
    SELECT
        CONCAT ('After swapping: a = ', a, ', b = ', b) AS AfterSwap;

END;


CALL swap_variables();