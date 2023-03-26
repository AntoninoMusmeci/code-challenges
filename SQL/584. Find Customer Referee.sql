/*
https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan&id=sql-i
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

*/
SELECT name
FROM Customer
WHERE referee_id IS NULL or referee_id <> 2