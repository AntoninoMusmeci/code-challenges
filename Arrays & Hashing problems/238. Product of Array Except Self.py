#https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prev_product = 1
        for i in range(len(nums)):
            result[i]*= prev_product
            prev_product *= nums[i]
        prev_product = 1
        for i in range(len(nums) -1,-1,-1):
            result[i]*= prev_product
            prev_product *= nums[i]
        return result