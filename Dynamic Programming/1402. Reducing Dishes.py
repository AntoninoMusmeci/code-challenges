#https://leetcode.com/problems/reducing-dishes/description/
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        tot = 0
        sum = 0
        for i in range(len(satisfaction)-1,-1,-1):
            if tot + sum + satisfaction[i] > tot:
                tot = tot + sum + satisfaction[i]
                sum = sum + satisfaction[i]
            else:
                return tot
        return tot