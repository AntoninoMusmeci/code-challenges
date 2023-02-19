class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)

        def dfs(node, parent):
            result = 0
            for neighbour in tree[node]:
                if neighbour != parent:
                    result += dfs(neighbour, node)
            if result or hasApple[node]:
                return result + 2
            return result
        return max(dfs(0, -1)-2, 0)
