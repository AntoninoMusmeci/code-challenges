#https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = {}
        for i in range(len(nums)):
            if (target-nums[i]) in num_pos:
                return [num_pos[target-nums[i]], i]
            else:
                num_pos[nums[i]] = i