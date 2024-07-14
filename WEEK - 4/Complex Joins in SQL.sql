-- Creating sample tables
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(50),
    EmployeeID INT
);

-- Inserting data
INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID) VALUES
(1, 'venu', 'sai', 1),
(2, 'venkat', 'Shreya', 2),
(3, 'vishal', 'hima', 3);

INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(1, 'HR'),
(2, 'Finance'),
(3, 'IT');

INSERT INTO Projects (ProjectID, ProjectName, EmployeeID) VALUES
(1, 'Project A', 1),
(2, 'Project B', 2),
(3, 'Project C', 3);

-- INNER JOIN: Returns records that have matching values in both tables
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID;

-- LEFT JOIN: Returns all records from the left table, and the matched records from the right table
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID;

-- RIGHT JOIN: Returns all records from the right table, and the matched records from the left table
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d ON e.DepartmentID = d.DepartmentID;


the END