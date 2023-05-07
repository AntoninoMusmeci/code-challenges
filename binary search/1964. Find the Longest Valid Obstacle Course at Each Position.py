#https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/description/
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        res = []
        dp = [10**8] * (n + 1)
        for obstacle in obstacles:
            index = bisect.bisect(dp, obstacle)
            res.append(index + 1)
            dp[index] = obstacle
        return res