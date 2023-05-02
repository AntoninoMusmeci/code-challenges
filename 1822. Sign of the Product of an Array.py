#https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                negatives += 1
        return -1 if negatives % 2 else 1