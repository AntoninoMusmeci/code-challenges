#https://leetcode.com/problems/number-of-operations-to-make-network-connected/editorial/
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        disconnected_graph = 0
        cycle_cable = 0
        visited = set()
        graph = {}
        def dfs(node,par):
            nonlocal cycle_cable
            visited.add(node)
            for nei in graph[node]:
                if nei in visited:
                    if nei != par:
                        cycle_cable += 1
                else:
                    dfs(nei,node)
        for i in range(n):
            graph[i] = []
        for connection in connections:
            c1 = connection[0]
            c2 = connection[1]
            graph[c1].append(c2)
            graph[c2].append(c1)
        for node in graph:
            if node not in visited:
                disconnected_graph += 1
                dfs(node,None)
        return (disconnected_graph - 1) if (disconnected_graph - 1) <= cycle_cable // 2 else -1