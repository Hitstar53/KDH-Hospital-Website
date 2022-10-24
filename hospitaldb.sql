-- @BLOCK
INSERT INTO doctors VALUES(1, 'Dr. John Doe', 'Cardiology', '1234567890', 'john@gmail.com', '12345678');
-- @BLOCK
DROP TABLE IF EXISTS appointments;
-- @BLOCK
DELETE FROM appointments WHERE id >= 1;