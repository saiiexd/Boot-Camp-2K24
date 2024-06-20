Introduction

SQL (Structured Query Language) includes several command types for managing and interacting with databases. These commands fall into three main categories: Data Definition Language (DDL), Data Manipulation Language (DML), and Data Control Language (DCL). Each category has a specific role in database management.

Data Definition Language (DDL)

DDL commands help define and manage the database structure, including tables, indexes, and schemas. These commands modify the database schema.

Common DDL Commands:

1. CREATE: This command creates new database objects like tables and indexes.

   Example:
   ```sql
   CREATE TABLE students (
       student_id INT PRIMARY KEY,
       name VARCHAR(50),
       age INT
   );
   ```

2. ALTER: This command changes the structure of existing database objects. It can add, delete, or modify columns in a table.

   Example:
   ```sql
   ALTER TABLE students ADD COLUMN email VARCHAR(100);
   ```

3. DROP: This command deletes database objects like tables and indexes.

   *Example:*
   ```sql
   DROP TABLE students;
   ```

4. TRUNCATE: This command removes all rows from a table but keeps the table structure intact.

   Example:
   ```sql
   TRUNCATE TABLE students;
   ```

5. RENAME: This command renames database objects.

   Example:
   ```sql
   ALTER TABLE students RENAME TO alumni;
   ```

Data Manipulation Language (DML)

DML commands handle data within database tables, allowing users to retrieve, insert, update, and delete data.

Common DML Commands:

1. SELECT: This command retrieves data from the database.

   Example:
   ```sql
   SELECT * FROM students;
   ```

2. INSERT: This command adds new rows to a table.

   Example:
   ```sql
   INSERT INTO students (student_id, name, age) VALUES (1, 'John Doe', 22);
   ```

3. UPDATE: This command modifies existing data in a table.

   Example:
   ```sql
   UPDATE students SET age = 23 WHERE student_id = 1;
   ```

4. DELETE: This command removes rows from a table.

   Example:
   ```sql
   DELETE FROM students WHERE student_id = 1;
   ```

Data Control Language (DCL)

DCL commands manage access permissions to the database, controlling who can perform various operations.

Common DCL Commands:

1. GRANT: This command grants specific access privileges to users.

   Example:
   ```sql
   GRANT SELECT, INSERT ON students TO 'username';
   ```

2. REVOKE: This command removes access privileges from users.

   Example:
   ```sql
   REVOKE SELECT, INSERT ON students FROM 'username';
   ```