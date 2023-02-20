#https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
class Solution:
    def countOrders(self, n: int) -> int:
        i = k = 1
        while i < 2*n:
            k *= (2*n - i)
            i = i + 2
        return (math.factorial(n) * k) % (10**9+7)