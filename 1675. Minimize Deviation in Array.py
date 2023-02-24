#https://leetcode.com/problems/minimize-deviation-in-array/description/
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        n_min = math.inf
        result = math.inf
        for n in nums:
            if n % 2 != 0:
                n = n*2
            n_min = min(n_min,n)
            max_heap.append(-1 * n)
        heapq.heapify(max_heap)
        while 1:
            n = heapq.heappop(max_heap) * -1
            result = min(result, n - n_min)
            if n % 2 != 0:
                break
            n = n//2
            n_min = min(n_min,n)
            heapq.heappush(max_heap, n * -1)
        return result
