#https://leetcode.com/problems/spiral-matrix-ii/description/
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        up = 0
        down = n - 1
        left = 0
        right = n - 1
        matrix = [[0]*n for _ in range(n)]
        i = 0
        while i < n**2:
            for j in range(left,right+1):
                matrix[up][j] = i + 1
                i+= 1
            for j in range(up+1,down+1):
                matrix[j][right] = i + 1
                i+= 1
            if up != down:
                for j in range(right-1,left-1,-1):
                    matrix[down][j] = i + 1
                    i+= 1
            if left != right:
                for j in range(down-1,up,-1):
                    matrix[j][left] = i + 1
                    i+= 1
            up += 1
            left += 1
            right -= 1
            down -= 1
        return matrix