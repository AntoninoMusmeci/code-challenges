#https://leetcode.com/problems/longest-cycle-in-a-graph/description/
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        set_visited = set()
        result = -1
        def dfs(edges, node, pos, visited):
            nonlocal result
            if node == -1:
                return
            visited[node] = pos
            set_visited.add(node)
            nei = edges[node]
            if nei in visited :
                result = max(result, pos - visited[nei] + 1)
            if nei not in set_visited:
                dfs(edges,nei,pos + 1, visited)
        for i in range(len(edges)):
            visited = {}
            if i not in set_visited:
                dfs(edges,i,0,visited)
        return result