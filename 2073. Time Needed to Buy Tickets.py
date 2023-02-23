#https://leetcode.com/problems/time-needed-to-buy-tickets/description/
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        for i in range(len(tickets)):
           result += min(tickets[i], (tickets[k] if i <= k else tickets[k] - 1))
        return result