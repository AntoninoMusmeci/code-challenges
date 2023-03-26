/*
https://leetcode.com/problems/big-countries/description/

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | int     |
+-------------+---------+
name is the primary key column for this table.
Each row of this table gives information about the name of a country, 
the continent to which it belongs, its area, the population, and its GDP value.
*/

SELECT name, population, area
FROM World
WHERE area >= 3000000 or population >= 25000000;