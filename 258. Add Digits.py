#https://leetcode.com/problems/add-digits/description/
class Solution:
    def addDigits(self, num: int) -> int:
        result = 0
        
        while num:
            result += num % 10
            num = num // 10 
            if result > 9:
                reminder = result % 10
                result = result // 10 + reminder
        return result
    
"""
This problem could be solved in O(1) time 

If we  list some solution we can find a pattern

1 = 1   2 = 2 ...  9 = 9
10 = 1  11= 2 ...  19 = 9
19 = 1  20 = 2     27 = 9

(n - 1) % 9 + 1

n = 12345

(12344) % 9 + 1  = 5

"""