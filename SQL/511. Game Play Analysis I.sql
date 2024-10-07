/*https://leetcode.com/problems/game-play-analysis-i/description/

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
*/

SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id