#https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicateSol1(self, nums: List[int]) -> bool:
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            else:
                num_set.add(n)
        return False

    def containsDuplicateSol2(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)