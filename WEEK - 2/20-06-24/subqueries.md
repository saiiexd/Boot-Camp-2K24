-- Subquery in the SELECT Clause
-- A subquery can be used in the SELECT clause to retrieve a value that will be used in the main query.

SELECT
    book_id,
    title,
    author,
    (SELECT category_name 
     FROM categories 
     WHERE categories.category_id = books.category_id) AS category_name
FROM
    books;

-- Subquery in the FROM Clause
-- A subquery can be used in the FROM clause to create a derived table that the main query can select from.

SELECT
    category_id,
    AVG(price) AS average_price
FROM
    (SELECT 
        category_id, 
        price 
     FROM 
        books) AS book_prices
GROUP BY
    category_id;

-- Subquery in the WHERE Clause
-- A subquery can be used in the WHERE clause to filter results based on a condition that involves another table or another row.

SELECT
    title
FROM
    books
WHERE
    category_id IN (SELECT category_id FROM categories WHERE category_name = 'Science Fiction');

-- Subquery with EXISTS
-- A subquery can be used with the EXISTS operator to check the existence of rows returned by the subquery.

SELECT
    title
FROM
    books b
WHERE
    EXISTS (SELECT 1 FROM categories c WHERE c.category_id = b.category_id);

-- Subquery with NOT EXISTS
-- A subquery can also be used with the NOT EXISTS operator to exclude rows that meet certain criteria.

SELECT
    title
FROM
    books b
WHERE
    NOT EXISTS (SELECT 1 FROM categories c WHERE c.category_id = b.category_id);

-- Subquery with ANY or ALL
-- Subqueries can be used with ANY or ALL to compare a value to a set of values returned by the subquery.

-- Any
SELECT
    title
FROM
    books
WHERE
    price > ANY (SELECT price FROM books WHERE category_id = 2);

-- All
SELECT
    title
FROM
    books
WHERE
    price > ALL (SELECT price FROM books WHERE category_id = 2);

-- Correlated Subqueries
-- A correlated subquery is a subquery that refers to a column from the outer query.

SELECT
    b1.title,
    b1.price
FROM
    books b1
WHERE
    b1.price > (SELECT AVG(b2.price) FROM books b2 WHERE b2.category_id = b1.category_id);
