#https://leetcode.com/problems/single-element-in-a-sorted-array/description/
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = 0
        while l < r:
            m = (r - l) //2 + l
            left_len = m - l  - (1 if nums[m] == nums[m-1] else 0)
            right_len = r - m  - (1 if nums[m] == nums[m+1] else 0) 
            if left_len == right_len:
                return nums[m]
            elif left_len % 2 != 0:
                r = l + left_len - 1
            else:
                l = r - right_len + 1
        return nums[l]