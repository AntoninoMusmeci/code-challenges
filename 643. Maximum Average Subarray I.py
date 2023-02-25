#https://leetcode.com/problems/maximum-average-subarray-i/description/
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        max_sum = current_sum = sum(nums[:k])
        for i in range(k,len(nums)):
            current_sum = current_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum / k