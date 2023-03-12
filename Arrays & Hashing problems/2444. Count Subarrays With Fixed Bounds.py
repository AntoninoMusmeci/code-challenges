class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        start = 0
        min_index = -1
        max_index = -1
        result = 0
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                start = i + 1
                min_index = -1
                max_index = -1 
                continue
            if nums[i] == maxK:
                max_index = i
            if nums[i] == minK:
                min_index = i
            #If min_index or max_index = -1, you should avoid summing the result => max(0, ...)
            result += max(0,min(min_index, max_index) - start + 1)
        return result