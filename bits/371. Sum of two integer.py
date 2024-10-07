class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        pos = 0
        while a != 0 or b != 0:
            a_bit = a & 1
            b_bit = b & 1
            res_bit = 0
            if carry == 0:
                res_bit = a_bit ^ b_bit
                carry = a_bit & b_bit
            else:
                res_bit = a_bit ^ b_bit
                if res_bit == 0:
                    res_bit = 1
                    carry = a_bit & b_bit
                
                else:
                    res_bit = 0
                    carry = 0
            a = a >> 1
            b = b >> 1
            result = result | (res_bit << pos)
            pos += 1

        if carry:
            result = result | (carry << pos)
        return result 
    




solution = Solution()
assert solution.getSum(1,9) == 10

assert solution.getSum(2,3) == 5