#https://leetcode.com/problems/can-place-flowers/description/
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        k = len(flowerbed)
        while i < k and n:
            if flowerbed[i] == 0:
                if i+1 == k or flowerbed[i+1] == 0:
                    n -= 1
                else: i += 1
            i+= 2
        return n == 0