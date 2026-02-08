-- 8. Use a PL/SQL block to delete item number 4 from the ITEM table.


use clg_std;

DROP PROCEDURE IF EXISTS delete_item;
CREATE PROCEDURE delete_item()
BEGIN
  DELETE FROM ITEM WHERE ItemNum = 4;
  SELECT 'Item with ItemNum 4 deleted' AS Info;
END;

CALL delete_item();
