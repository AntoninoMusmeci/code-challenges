/*
https://leetcode.com/problems/customers-who-never-order/description

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID and name of a customer.
*/

SELECT name as Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders)