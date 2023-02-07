#https://leetcode.com/problems/fruit-into-baskets/
class Solution:
    def totalFruit(self, fruits):
        basket = {}
        i = 0
        j = 0
        max_len = 0
        for j in range(len(fruits)):
            basket[fruits[j]] = basket.get(fruits[j], 0) + 1
            while len(basket) > 2:
                basket[fruits[i]] -= 1
                if  basket[fruits[i]] == 0:
                    del basket[fruits[i]]
                i+= 1
            
            max_len = max(max_len, j - i + 1)

        return max_len