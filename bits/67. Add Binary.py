# https://leetcode.com/problems/add-binary/description/
from itertools import zip_longest
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        for x, y in zip_longest(a[::-1], b[::-1], fillvalue="0"):
            x = int(x)
            y = int(y)
            digit = (x + y + carry) % 2
            carry = (x + y + carry) // 2
            result += str(digit)
        if carry == 1:
            result += "1"
        return result[::-1]
