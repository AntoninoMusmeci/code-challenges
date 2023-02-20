#https://leetcode.com/problems/search-insert-position/description/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l
            if nums[m] == target:
                return m
            if nums[m] > target:
                #target must be to the left
                r = m - 1
            else:
                #target must be to the right
                l = m + 1
        return r + 1