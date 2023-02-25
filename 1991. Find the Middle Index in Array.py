# https://leetcode.com/problems/find-the-middle-index-in-array/description/
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        prev = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            left_sum += prev
            right_sum -= nums[i]
            prev = nums[i]
            if left_sum == right_sum:
                return i
        return - 1
