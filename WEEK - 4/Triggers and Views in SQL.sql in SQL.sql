-- Creating a sample table
CREATE TABLE EmployeeChanges (
    ChangeID INT AUTO_INCREMENT PRIMARY KEY,
    EmployeeID INT,
    ChangeDate DATETIME,
    OldFirstName VARCHAR(50),
    NewFirstName VARCHAR(50)
);

-- Creating the trigger
DELIMITER $$
CREATE TRIGGER BeforeEmployeeUpdate
BEFORE UPDATE ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO EmployeeChanges (EmployeeID, ChangeDate, OldFirstName, NewFirstName)
    VALUES (OLD.EmployeeID, NOW(), OLD.FirstName, NEW.FirstName);
END $$
DELIMITER ;
