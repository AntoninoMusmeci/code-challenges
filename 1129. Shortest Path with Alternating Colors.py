#https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
import collections
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        distances = [[0.0, 0.0]] + [[float("inf"), float("inf")] for i in range(n - 1)]
        graph = [[[],[]] for _ in range(n)]
        for edge in redEdges:
            graph[edge[0]][0].append(edge[1])
        for edge in blueEdges:
            graph[edge[0]][1].append(edge[1])
        queue = collections.deque([[0, 0], [0, 1]])
        while queue:
            current_node, current_color = queue.popleft()
            for neighbour in graph[current_node][current_color]:
                if distances[neighbour][current_color] == float("inf"):
                    distances[neighbour][current_color] = 1 + distances[current_node][1 - current_color]
                    queue.append([neighbour,1-current_color])
        return [int(x) if x < float("inf") else -1 for x in map(min, distances)]