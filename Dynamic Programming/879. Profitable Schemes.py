#https://leetcode.com/problems/profitable-schemes/description/
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        
        cache = {}
        def dfs(i,people,tot_profit):
            if (i,people,tot_profit) in cache:
                return cache[(i,people,tot_profit)]
            if people <= 0 or i >= len(profit):
                return 1 if tot_profit >= minProfit else 0
            tot = 0
            if people - group[i] >= 0:
                tot += dfs(i+1,people - group[i], min(minProfit,tot_profit + profit[i]))
                cache[(i+1,people-group[i],tot_profit+profit[i])] = tot

            tot += dfs(i+1,people,min(minProfit,tot_profit))
            cache[(i,people,tot_profit)] = tot
            return tot
      
        return dfs(0,n,0) % (10**9 +7)