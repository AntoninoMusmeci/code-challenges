#https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) -1
        max_area = min(height[l],height[r]) * (r - l) 
        while l < r:        
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area,min(height[l],height[r]) * (r - l))
        return max_area