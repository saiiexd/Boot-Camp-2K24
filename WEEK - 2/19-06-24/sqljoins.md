### 1. INNER JOIN

- Description: Returns only the rows where there is a match in both tables.

  ```sql
  SELECT *
  FROM table1
  INNER JOIN table2 ON table1.common_column = table2.common_column;
  ```

### 2. LEFT JOIN

- Description: Returns all rows from the left table and the matched rows from the right table. If no match, NULLs are returned for right table columns.

  ```sql
  SELECT *
  FROM table1
  LEFT JOIN table2 ON table1.common_column = table2.common_column;
  ```

### 3. RIGHT JOIN

- Description: Returns all rows from the right table and the matched rows from the left table. If no match, NULLs are returned for left table columns.

  ```sql
  SELECT *
  FROM table1
  RIGHT JOIN table2 ON table1.common_column = table2.common_column;
  ```

### 4. FULL JOIN (or FULL OUTER JOIN)

- Description: Returns rows when there is a match in one of the tables. Rows without matches in either table will have NULLs for the missing values.

  ```sql
  SELECT *
  FROM table1
  FULL JOIN table2 ON table1.common_column = table2.common_column;
  ```
