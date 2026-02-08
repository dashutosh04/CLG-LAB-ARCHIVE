-- 1. Write a PL/SQL block to calculate the area of a circle. Declare PI as constant.

USE clg_std;

DROP PROCEDURE IF EXISTS CalcArea;

CREATE PROCEDURE CalcArea() 
  BEGIN 
    DECLARE PI DECIMAL(10, 8) DEFAULT 3.14159265;
    DECLARE radius DECIMAL(10, 2) DEFAULT 5;
    DECLARE area DECIMAL(10, 2);

    SET
      area = PI * radius * radius;

    SELECT
      CONCAT ('Area of circle of r =', radius,' is: ',area
      ) AS Result;

END;

CALL CalcArea ();