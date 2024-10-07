# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int: 
    ##################################  RECURSIVE  ##################################
        # cache = {}
        # def dp(target,n):
        #     if n == 0:
        #         return 1 if target == 0 else 0
        #     if (target,n) in cache:
        #         return cache[(target,n)]
        #     res = 0
        #     for face in range(1,k+1):
        #         res += dp(target - face, n - 1)
        #     cache[(target,n)] = res
        #     return res
        # return dp(target,n) % (10**9 + 7)

    ##################################  BOTTOM UP  ##################################


        row = [0] *  (target + 1) 
        row[0] = 1
        
        for dice in range(n):
            new_row = [0] * (target + 1) 
            for t in range(dice,target + 1):
                for val in range(1,k+1):
                    new_row[t] += row[t - val] if (t - val) >= 0 else 0
            row = new_row
        return row[-1] % (10**9 + 7)
        
        