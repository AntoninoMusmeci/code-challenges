import collections
class Solution(object):
    def numberOfGoodSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        count = collections.Counter(nums)
        primes_masks = [sum(1<<i for i, p in enumerate(good_numbers) if x % p == 0) 
            for x in range(31)]
        
        def count_subsets(n, mask):
            if n == 1:
                return 1
            result = count_subsets(n - 1, mask)
            if n % 4 != 0 and n % 9 != 0 and n % 25 != 0 and mask & primes_masks[n] ==  0:
                result += count_subsets(n -  1, mask | primes_masks[n]) * count[n]
            return result
        mod = 10**9 + 7
 
        return ( (count_subsets(30, 0) - 1)* pow(2,count[1], mod)) % mod