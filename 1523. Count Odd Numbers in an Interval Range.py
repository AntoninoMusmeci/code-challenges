#https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (1 if low % 2 != 0 or high % 2 != 0 else 0)