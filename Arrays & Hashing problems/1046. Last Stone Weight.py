#https://leetcode.com/problems/last-stone-weight/description/
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)
            remain = abs(s1-s2)
            if remain > 0:
                heapq.heappush(stones,-remain)
        return -stones[0] if len(stones) > 0 else 0