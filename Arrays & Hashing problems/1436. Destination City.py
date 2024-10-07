#https://leetcode.com/problems/destination-city/
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        graph = defaultdict(list)
        for path in paths:
            graph[path[0]].append(path[1])
            graph[path[1]] += []          
        for path in graph:
            if len(graph[path]) == 0:
                return path