#https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/editorial/
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        number_of_nodes = 0
        graph = {}
        result = 0
        def dfs(node, visited):
            nodes = 0
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    nodes += 1 + dfs(nei, visited)
            return nodes
        while n:
            graph[n - 1] = []
            n-= 1
        for edge in edges:
            n1,n2 = edge
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()
        for node in graph:
            if node not in visited:
                current_nodes = 1 + dfs(node, visited)
                result+= current_nodes * number_of_nodes
                number_of_nodes += current_nodes
        return result
