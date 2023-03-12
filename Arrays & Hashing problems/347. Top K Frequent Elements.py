#https://leetcode.com/problems/top-k-frequent-elements/
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        heap = []
        result = []
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        for n in counter.keys():
            heap.append((-counter[n],n))
        heapq.heapify(heap)
        while k:
            k-= 1
            result.append(heapq.heappop(heap)[1])
        return result