
### DDL (Data Definition Language):

DDL is used to define or modify the structure of database objects such as tables, indexes, and constraints.

1. Create Table:
   ```sql
   CREATE TABLE IF NOT EXISTS students (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(50),
       age INT,
       grade VARCHAR(10)
   );
   ```

2. Alter Table (Adding a Column):
   ```sql
   ALTER TABLE students
   ADD COLUMN email VARCHAR(255);
   ```

3. Drop Table:
   ```sql
   DROP TABLE IF EXISTS students;
   ```

### DML (Data Manipulation Language):

DML is used to manipulate data within database objects like tables.

1. Insert Data:
   ```sql
   INSERT INTO students (name, age, grade, email)
   VALUES ('Alice', 18, 'A', 'alice@example.com'),
          ('Bob', 20, 'B', 'bob@example.com'),
          ('Charlie', 19, 'B', 'charlie@example.com');
   ```

2. Update Data:
   ```sql
   UPDATE students
   SET grade = 'A'
   WHERE name = 'Alice';
   ```

3. Delete Data:
   ```sql
   DELETE FROM students
   WHERE name = 'Bob';
   ```

### DCL (Data Control Language):

DCL is used to control access and permissions in the database.

1. Grant Privileges:
   ```sql
   GRANT SELECT, INSERT, UPDATE, DELETE ON students TO 'user1'@'localhost' IDENTIFIED BY 'password';
   ```

2. Revoke Privileges:
   ```sql
   REVOKE DELETE ON students FROM 'user1'@'localhost';
   ```
