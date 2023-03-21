#https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_zero = 0
        result = 0
        for n in nums:
            if n != 0:
                result += num_zero * (num_zero+1) // 2
                num_zero = 0
            else: num_zero += 1
        result +=  num_zero * (num_zero+1) // 2
        return result