#https://leetcode.com/problems/move-zeroes/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_index = i = 0
        while i < len(nums):
            while zero_index < len(nums) and nums[zero_index] != 0:
                zero_index += 1
            if zero_index >= len(nums):
                break
            if i > zero_index:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
            i+= 1
        return nums