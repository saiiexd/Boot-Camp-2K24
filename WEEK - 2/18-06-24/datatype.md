#data types define the type of data that can be stored in a column of a table. Each data type has specific properties and storage requirements.


1. Numeric Data Types:
   - `INT`: Integer data type for whole numbers.
     ```sql
     age INT;
     ```

   - `FLOAT`: Floating-point data type for approximate numeric values.
     ```sql
     price FLOAT(10, 2); -- Total digits: 10, Decimal places: 2
     ```

   - `DOUBLE`: Double-precision floating-point data type for larger numeric values.
     ```sql
     amount DOUBLE;
     ```

2. String Data Types:
   - `VARCHAR`: Variable-length string data type.
     ```sql
     name VARCHAR(50); -- Maximum 50 characters
     ```

   - `CHAR`: Fixed-length string data type.
     ```sql
     country CHAR(3); -- Always 3 characters
     ```

   - `TEXT`: Large text data type.
     ```sql
     description TEXT;
     ```

3. Date and Time Data Types:
   - `DATE`: Date data type.
     ```sql
     dob DATE;
     ```

   - `DATETIME`: Date and time data type.
     ```sql
     created_at DATETIME;
     ```

   - `TIMESTAMP`: Automatic timestamp data type.
     ```sql
     updated_at TIMESTAMP;
     ```

4. Boolean Data Type:
   - `BOOLEAN` or `BOOL`: Boolean data type.
     ```sql
     is_active BOOLEAN;
     ```

5. Binary Data Types:
   - `BLOB`: Binary large object data type.
     ```sql
     image BLOB;
     ```

6. Enum and Set Data Types:
   - `ENUM`: Enumeration data type.
     ```sql
     status ENUM('active', 'inactive', 'pending');
     ```

   - `SET`: Set data type.
     ```sql
     permissions SET('read', 'write', 'delete');
     ```

