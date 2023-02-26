#https://leetcode.com/problems/last-stone-weight-ii/description/
from functools import lru_cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
    #The goal is to divide the stones into two groups that are as similar in weight as possible.

        total_weight = sum(stones)
        target = math.ceil(total_weight / 2) 
        @lru_cache(None)
        def dfs(i,total):
            if i >= len(stones) - 1 or total >= target:
                return abs(total - (total_weight - total))
            return min(dfs(i+1,total), dfs(i+1,total + stones[i+1]))
        return dfs(0,0)