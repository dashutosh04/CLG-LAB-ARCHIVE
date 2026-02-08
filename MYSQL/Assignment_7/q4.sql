-- 4. Write a PL/SQL program to input hours and rate. Find gross pay and net pay. The tax rate is 28%.

use clg_std;

DROP PROCEDURE IF EXISTS calc_pay;
CREATE PROCEDURE calc_pay()
BEGIN
  DECLARE hours DECIMAL(10,2) DEFAULT 40;
  DECLARE rate DECIMAL(10,2) DEFAULT 25;
  DECLARE gross_pay DECIMAL(10,2);
  DECLARE net_pay DECIMAL(10,2);
  DECLARE tax_rate DECIMAL(10,2) DEFAULT 0.28;
  SET gross_pay = hours * rate;
  SET net_pay = gross_pay - (gross_pay * tax_rate);
  SELECT CONCAT('Gross Pay: ', gross_pay, ', Net Pay: ', net_pay) AS PayInfo;
END;

CALL calc_pay();