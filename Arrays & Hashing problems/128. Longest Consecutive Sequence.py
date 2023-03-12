#https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        prev_val = 0
        values = set(nums)
        for n in nums:
            current_len = 0
            if (n-1) not in values:
                while n in values:
                    n += 1
                    current_len += 1
            max_len = max(max_len, current_len)
        return max_len