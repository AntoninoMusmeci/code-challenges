# https://leetcode.com/problems/similar-string-groups/description/
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def isSimilar(a, b):
            diff_chars = 0
            for i in range(0, len(a)):
                if a[i] != b[i]:
                    diff_chars += 1
                if diff_chars > 2:
                    return False
            return diff_chars <= 2
        graph = {}
        visited = set()
        result = 0
        m = len(strs)
        n = len(strs[0])
        for i in range(0, m):
            for j in range(i+1, m):

                if j not in graph:
                    graph[j] = []
                if i not in graph:
                    graph[i] = []
                if isSimilar(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        print(graph)

        def bfs(start):
            visited.add(start)
            for nei in graph[start]:
                if nei not in visited:
                    bfs(nei)
        for i in range(m):
            if i not in visited:
                result += 1
                bfs(i)
        return result
