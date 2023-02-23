
#https://leetcode.com/problems/ipo/description/

# TIME LIMIT EXCEDED
# class Solution:
#     def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
#         n = len(profits)
#         profit_to_capitals = {}
#         for i in range(n):
#             if profits[i] not in profit_to_capitals:
#                 profit_to_capitals[profits[i]] = [capital[i]]
#             else:
#                 profit_to_capitals[profits[i]].append(capital[i])
#         for p in profit_to_capitals:
#             profit_to_capitals[p].sort()
#         profits.sort(reverse=True)
#         j = min(k, n)
#         pointers = { key:0 for key in profit_to_capitals.keys()}
#         while j > 0:
#             j -= 1
#             for p in profits:
#                 if p in profit_to_capitals:
#                     pointer = pointers[p]
#                     if pointer < len(profit_to_capitals[p]) and w >= profit_to_capitals[p][pointer] :
#                         w += p
#                         pointers[p] += 1
#                         break
#         return w


# Solution using 2 Heap

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        capital_heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(capital_heap)
        profits_heap = []

        while k > 0:
            while capital_heap and capital_heap[0][0] <= w:
                c, p = heapq.heappop(capital_heap)
                heapq.heappush(profits_heap, -1 * p)
            if not profits_heap:
                break
            w += -1 * heapq.heappop(profits_heap)
            k -= 1
        return w


# 1 heap
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        capital_profits = [(c, p) for c, p in zip(capital, profits)]
        capital_profits.sort()
        profits_heap = []
        i = 0
        while k > 0:
            while i < len(capital_profits) and capital_profits[i][0] <= w:
                p = capital_profits[i][1]
                heapq.heappush(profits_heap, -1 * p)
                i += 1
            if not profits_heap:
                break
            w += -1 * heapq.heappop(profits_heap)
            k -= 1
        return w
