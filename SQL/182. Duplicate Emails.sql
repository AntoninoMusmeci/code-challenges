/*
#https://leetcode.com/problems/duplicate-emails/description/
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
*/

SELECT email as Email
FROM Person
GROUP BY email
HAVING count(*) > 1