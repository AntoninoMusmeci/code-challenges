
#https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        points.sort()
        res = 0
        for i in range(1,len(points)):
            res = max(res, points[i][0] - points[i - 1][0])
        return res
        