-- Find each employee’s salary information and level based on the salary.
USE corp_emp;

SELECT
    emp.Salary,
    empl.LevelNo
FROM
    employee AS emp
    CROSS JOIN emplevel AS empl ON emp.Salary BETWEEN empl.LowSalary AND empl.HighSalary;