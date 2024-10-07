#https://leetcode.com/problems/buy-two-chocolates/submissions/

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        min1 = float('inf')
        min2 = float('inf')
        for p in prices:
            if p < min1:
                min1,min2 = p, min1
            elif p < min2:
                min2 = p
        cost = min1+min2
        return money-cost if cost <= money else money 