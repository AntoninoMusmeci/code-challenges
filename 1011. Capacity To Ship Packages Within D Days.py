#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = (r - l) //2 + l
            current_day_weights = 0
            current_days = 1
            for w in weights:
               current_day_weights += w
               if current_day_weights > m:
                   current_day_weights = w
                   current_days += 1
            if current_days > days:
                l = m + 1
            else:
                r = m
        return l