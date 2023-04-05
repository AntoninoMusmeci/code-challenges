#https://leetcode.com/problems/minimize-maximum-of-array/description/
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        result = nums[0]
        currentSum = nums[0]
        for i in range(1,len(nums)):

            currentSum += nums[i]
            result = max(result,math.ceil(currentSum / (i+1)))

        return result