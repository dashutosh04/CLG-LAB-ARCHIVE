-- 9. Write a PL/SQL block to ask a user to input a valid employee Id. 
-- Retrieve employees name, qualification description, salary and commission. 
-- Print name, qualification and sum of salary and commission.

use corp_emp;

DROP PROCEDURE IF EXISTS get_employee_details;
CREATE PROCEDURE get_employee_details(IN empId INT)
BEGIN
  DECLARE empName VARCHAR(100);
  DECLARE qualDes VARCHAR(100);
  DECLARE sal DECIMAL(10,2);
  DECLARE comm DECIMAL(10,2);
  DECLARE total_pay DECIMAL(10,2);
  DECLARE q_id INT;
  
  SELECT CONCAT(Fname," ",Lname), salary, commission, QualId
    INTO empName, sal, comm, q_id
  FROM EMPLOYEE
  WHERE EmployeeId = empId;
  
  SELECT QualDesc
  INTO QualDes
  FROM qualification
  WHERE q_id = QualId;
  
  SET total_pay = sal + comm;
  
  SELECT empName AS Employee_Name ,qualDes,total_pay;
END;

CALL get_employee_details(2);

