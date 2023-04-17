#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxn= max(candies)
        return [c + extraCandies >= maxn for c in candies ]