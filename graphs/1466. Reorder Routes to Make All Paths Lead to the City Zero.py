#https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        result = 0
        graph = {}
        for connection in connections:
            c1,c2 = connection
            if c1 not in graph:
                graph[c1] = []
            if c2 not in graph:
                graph[c2] = []
            graph[c1].append((c2, +1))
            graph[c2].append((c1,0))
        
        def dfs(node, par):
            nonlocal result
            for nei in graph[node]:
                if nei[0] != par:
                    result += nei[1]
                    dfs(nei[0],node)
        dfs(0,None)
        return result