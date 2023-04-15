#https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/description/
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        
        cache = {}
        def selectCoins(pile,remain_coins):
           
            if pile >= len(piles) or remain_coins == 0:
                return 0
            if (pile,remain_coins) in cache:
                return cache[(pile,remain_coins)]
            tot = 0
            tot += selectCoins(pile+1,remain_coins)
            sum = 0
            for i in range(min(len(piles[pile]),remain_coins)):
                sum += piles[pile][i]
                tot = max(tot, sum + selectCoins(pile + 1,remain_coins - 1 - i) )
            cache[(pile,remain_coins)] = tot
            return tot


        return selectCoins(0,k)