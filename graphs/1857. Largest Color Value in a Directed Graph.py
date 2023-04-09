#https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        graph = {}
        mem = {}
        """
        {0: [1,2]
         1: []
         ...}
        """ 
        n = len(colors)
        for i in range(n):
            graph[i] = []
            mem[i] = [0] * 26
            completed = set()
        for edge in edges:
            graph[edge[0]].append(edge[1])
        result = 0
        cycle = False
        def dfs(start, visited):
            nonlocal cycle
            if start in completed:
                return mem[start]        
            for nei in graph[start]:
                if nei in visited:
                    cycle = True
                    return
                visited.add(nei)
                dfs(nei, visited)
                if cycle:
                    return
                for i,c in enumerate(mem[nei]):
                    mem[start][i] = max(mem[start][i], c)
                visited.remove(nei)
            mem[start][ord(colors[start]) - ord('a')] += 1
            completed.add(start)
            return
            
        
        for node in graph:
            dfs(node,set())
            if not cycle:
                result = max(result,max(mem[node]))
            else:
                return -1
        return result