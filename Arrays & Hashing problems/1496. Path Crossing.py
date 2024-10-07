#https://leetcode.com/problems/path-crossing/description/
class Solution:
    def isPathCrossing(self, path: str) -> bool:

        visited = set()
        visited.add((0,0))
        dir = {
            'N':(0,1), 
            'S':(0,-1), 
            'E':(1,0),
            'W':(-1,0)
        }
        
        current = (0,0)
        for p in path:
            current = (current[0] + dir[p][0],current[1] + dir[p][1])
            if current in visited:
                return True
            visited.add(current)
        return False
