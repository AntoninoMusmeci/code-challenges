#https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
import math
class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = {}
        min_w = math.inf
        def dfs(start, end, visited):
            visited.add(start)
            nonlocal min_w       
            for nei in graph[start]:
                 min_w = min(min_w, nei[1])
                 if nei[0] not in visited:
                   dfs(nei[0],end,visited)

        for i in range(len(roads)):
            c1,c2,w = roads[i]
            if c1 not in graph:
                graph[c1] = []
            if c2 not in graph:
                graph[c2] = []
            graph[c1].append((c2,w))
            graph[c2].append((c1,w))
        dfs(1,n,set())
        return min_w