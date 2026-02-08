-- 2. Write a PL/SQL block to find the square, cube, and double of a number.
use clg_std;

DROP PROCEDURE IF EXISTS num_operations;

CREATE PROCEDURE num_operations() 
BEGIN 
  DECLARE num INT DEFAULT 3;
  DECLARE square INT;
  DECLARE cub INT;
  DECLARE dbl INT;
  SET
    square = num * num;
  SET
    cub = num * num * num;
  SET
    dbl = num * 2;
  SELECT
    CONCAT (
      'Number: ',
      num,
      ', Square: ',
      square,
      ', Cube: ',
      cub,
      ', Double: ',
      dbl
    ) AS Result;

END;

CALL num_operations();