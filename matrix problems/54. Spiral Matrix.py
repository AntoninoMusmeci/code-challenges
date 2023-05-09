class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix) #num of rows
        n = len(matrix[0]) #num of columns
        up = 0
        down = m - 1
        left = 0
        right = n - 1
        result = []
        while len(result) < n * m:
            for j in range(left,right +1):
                result.append(matrix[up][j])
            for j in range(up+1,down + 1):
                result.append(matrix[j][right])
            if up != down:
                for j in range(right-1,left - 1,-1):
                    result.append(matrix[down][j])
            if left != right:
                for j in range(down-1,up,-1):
                    result.append(matrix[j][left])
            up += 1
            left+=1
            right -= 1
            down -= 1
        return result
    