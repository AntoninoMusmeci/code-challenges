#https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        return [set_nums1-set_nums2, set_nums2-set_nums1]