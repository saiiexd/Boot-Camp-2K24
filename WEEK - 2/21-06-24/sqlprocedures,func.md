-- Create the database
CREATE DATABASE schoolManagementDB;
USE schoolManagementDB;

-- Create students table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    class_id INT,
    gpa DECIMAL(3, 2),
    enrollment_date DATE
);

-- Create classes table
CREATE TABLE classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50),
    teacher_id INT
);

-- Create teachers table
CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- Create stored procedure GetStudentsByClass
DELIMITER //

CREATE PROCEDURE GetStudentsByClass(IN class_id INT)
BEGIN
    SELECT 
        student_id, first_name, last_name, gpa, enrollment_date 
    FROM 
        students 
    WHERE 
        class_id = class_id;
END //

DELIMITER ;

-- Create stored function GetAverageGPA
DELIMITER //

CREATE FUNCTION GetAverageGPA(class_id INT) RETURNS DECIMAL(3, 2)
BEGIN
    DECLARE avg_gpa DECIMAL(3, 2);
    SELECT AVG(gpa) INTO avg_gpa
    FROM students
    WHERE class_id = class_id;
    RETURN avg_gpa;
END //

DELIMITER ;

-- Create procedure UpdateGPA using cursor
DELIMITER //

CREATE PROCEDURE UpdateGPA(class_id INT)
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE student_id INT;
    DECLARE student_gpa DECIMAL(3, 2);

    -- Declare a cursor to select student IDs and their GPAs
    DECLARE student_cursor CURSOR FOR 
        SELECT student_id, gpa 
        FROM students 
        WHERE class_id = class_id;

    -- Declare a handler to set the done variable when there are no more rows
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN student_cursor;

    student_loop: LOOP
        FETCH student_cursor INTO student_id, student_gpa;
        IF done THEN
            LEAVE student_loop;
        END IF;

        -- Update each student's GPA by adding 0.1 (arbitrary example)
        UPDATE students 
        SET gpa = student_gpa + 0.1 
        WHERE student_id = student_id;
    END LOOP;

    CLOSE student_cursor;
END //

DELIMITER ;

-- To call this procedure:
CALL UpdateGPA(1);
