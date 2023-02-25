#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        max_price = 0
        profit = 0
        for p in  prices:
            if p < min_price:
                min_price = max_price = p
            max_price = max(p, max_price)
            profit = max(profit, max_price - min_price)
        return profit
                