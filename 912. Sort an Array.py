#https://leetcode.com/problems/sort-an-array/description/
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result = []
        heapq.heapify(nums)
        while nums:
            result.append(heapq.heappop(nums))
        return result