#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            while numbers[r] > target - numbers[l]:
                r -= 1
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            l += 1