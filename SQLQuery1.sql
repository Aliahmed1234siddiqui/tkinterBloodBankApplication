CREATE DATABASE BloodBanKApplication;

CREATE TABLE Reg(
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Contact VARCHAR(20),
    BloodGroup VARCHAR(5),
	email VARCHAR(225),
	
);
SELECT * FROM Reg;

ALTER TABLE Reg ADD bottle VARCHAR(2) Null;
UPDATE Reg SET bottle = '4' WHERE Name = 'aliyan' AND ID = 123123;


