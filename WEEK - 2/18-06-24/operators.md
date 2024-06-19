MySQL supports various operators that are used for performing operations on data. Here are some common operators in MySQL along with code examples:

### Arithmetic Operators:
1. Addition (`+`):
   ```sql
   SELECT 10 + 5; -- Result: 15
   ```

2. Subtraction (`-`):
   ```sql
   SELECT 20 - 8; -- Result: 12
   ```

3. Multiplication (`*`):
   ```sql
   SELECT 5 * 4; -- Result: 20
   ```

4. Division (`/`):
   ```sql
   SELECT 25 / 5; -- Result: 5
   ```

5. Modulus (`%`):
   ```sql
   SELECT 15 % 4; -- Result: 3 (Remainder of 15 divided by 4)
   ```

### Comparison Operators:
1. Equal to (`=`):
   ```sql
   SELECT * FROM users WHERE age = 25;
   ```

2. Not equal to (`<>` or `!=`):
   ```sql
   SELECT * FROM users WHERE status <> 'inactive';
   ```

3. Greater than (`>`):
   ```sql
   SELECT * FROM products WHERE price > 100;
   ```

4. Less than (`<`):
   ```sql
   SELECT * FROM orders WHERE total_amount < 500;
   ```

5. Greater than or equal to (`>=`):
   ```sql
   SELECT * FROM employees WHERE salary >= 50000;
   ```

6. Less than or equal to (`<=`):
   ```sql
   SELECT * FROM products WHERE stock <= 10;
   ```

### Logical Operators:
1. AND (`AND` or `&&`):
   ```sql
   SELECT * FROM customers WHERE age >= 18 AND country = 'USA';
   ```

2. OR (`OR` or `||`):
   ```sql
   SELECT * FROM users WHERE role = 'admin' OR role = 'manager';
   ```

3. NOT (`NOT` or `!`):
   ```sql
   SELECT * FROM products WHERE NOT status = 'sold';
   ```

### String Concatenation Operator:
1. Concatenation (`CONCAT()` or `||`):
   ```sql
   SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;
   ```

### Assignment Operator:
1. Assignment (`=`):
   ```sql
   UPDATE students SET grade = 'A' WHERE id = 1;
   ```