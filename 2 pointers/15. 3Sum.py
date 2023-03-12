#https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def findTwoSum(nums,start, k):
            l = start
            r = len(nums) - 1
            while l < r:
                while nums[r] + nums[k] + nums[l] > 0 and r > l:
                    r -= 1
                if nums[r] + nums[l] + nums[k] == 0 and l != r:
                    result.append([nums[k], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
        for i in range(0,len(nums) - 2):
            if nums[i] > 0:
                break
            if i ==0  or nums[i] != nums[i-1]:
                findTwoSum(nums,i+1,i)
        return result