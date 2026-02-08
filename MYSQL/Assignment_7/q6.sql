-- 6. Create a table called ITEM with one column ItemNum with NUMBER type. Write a PL/SQL program to insert values of 1 to 5 for ItemNum.
USE clg_std;

DROP TABLE IF EXISTS ITEM;

CREATE TABLE
    ITEM (ItemNum INT);

DROP PROCEDURE IF EXISTS insert_item_values;
CREATE PROCEDURE insert_item_values()
BEGIN DECLARE i INT DEFAULT 1;

WHILE i <= 5 DO
INSERT INTO
    ITEM (ItemNum)
VALUES
    (i);

SET
    i = i + 1;

END WHILE;

END;

CALL insert_item_values ();

SELECT
    *
FROM
    ITEM;