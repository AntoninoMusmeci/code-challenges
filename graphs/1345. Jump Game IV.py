# https://leetcode.com/problems/jump-game-iv/description/
class Solution:
    def minJumps(self, arr: List[int]) -> int:

        values_indices = {}
        for i, v in enumerate(arr):
            if v not in values_indices:
                values_indices[v] = [i]
            else:
                values_indices[v].append(i)

        current = [0]
        visited = {0}
        steps = 0

        # bfs
        while current:
            next = []

            for node in current:
                if node == len(arr) - 1:
                    return steps
                for i in values_indices[arr[node]]:
                    if i not in visited:
                        visited.add(i)
                        next.append(i)
                values_indices[arr[node]] = []
                for i in [node-1, node+1]:
                    if 0 <= i < len(arr) and i not in visited:
                        visited.add(i)
                        next.append(i)
                current = next
            steps += 1
        return -1
