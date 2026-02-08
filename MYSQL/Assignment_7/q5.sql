-- 5. Write a PL/SQL block to print all odd numbers between 1 and 10 using a loop.

use clg_std;

DROP PROCEDURE IF EXISTS print_odds;
CREATE PROCEDURE print_odds()
BEGIN
  DECLARE i INT DEFAULT 1;
  WHILE i <= 10 DO
    IF MOD(i, 2) <> 0 THEN
      SELECT i AS OddNumber;
    END IF;
    SET i = i + 1;
  END WHILE;
END;

CALL print_odds;