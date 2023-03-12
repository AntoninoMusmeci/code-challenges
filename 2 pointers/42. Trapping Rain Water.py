#https://leetcode.com/problems/trapping-rain-water/description/
class Solution:
    def trap(self, height: List[int]) -> int:
        wl = 0
        wr = len(height) - 1
        l = 0
        r = wr
        water = 0
        while l < r:
            if height[wl] <= height[wr]:
                l += 1
                if height[l] <= height[wl]:
                    water += height[wl] - height[l]
                else:
                    wl = l
            else:
                r -= 1
                if height[r] <= height[wr]:
                    water += height[wr] - height[r]
                else:
                    wr = r
        return water
    