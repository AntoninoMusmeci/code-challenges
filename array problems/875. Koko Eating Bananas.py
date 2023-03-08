#https://leetcode.com/problems/koko-eating-bananas/description/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def hours_to_eat(k):
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / k)
            return total_hours

        while l < r:
            k = (r - l) //2 + l
            hours = hours_to_eat(k)
            if hours > h:
                l = k + 1
            else:
                r = k
        return l