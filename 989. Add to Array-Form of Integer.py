#https://leetcode.com/problems/add-to-array-form-of-integer/description/
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        while k != 0 and i >= 0:
            #retrive last digit of the number k
            digit = k % 10
            #remove last digit from k
            k = k // 10
            #add digit to the num array. i keep track of the current position on num
            current_sum = (num[i] + digit) % 10
            k += (num[i] + digit) // 10
            num[i] = current_sum
            i-= 1
        if k != 0:
            num = list(map(int, str(k))) + num
        return num
