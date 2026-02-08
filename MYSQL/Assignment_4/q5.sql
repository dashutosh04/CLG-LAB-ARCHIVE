.--  Create a new user XYZ and grant only SELECT privilege to the user on your TERM table.


CREATE USER 'XYZ'@'%' IDENTIFIED BY '123';

GRANT SELECT ON clg_std.term TO 'XYZ'@'%';

FLUSH PRIVILEGES;


-- Query OK, 0 rows affected (0.04 sec)
