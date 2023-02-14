#https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/description/
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = flip_sum = index_sum = 0
        """[1, i] are ones if the all the flips' element in the range [1, i] are ones are all the numbers between 1 and i. => the sum of the index have to be equal to the  sum of the flips elements"""
        for i in range(len(flips)):
            flip_sum += i + 1
            index_sum += flips[i]
            res += flip_sum == index_sum
        return res