#https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_col = len(matrix[0])
        l = 0
        r = n_rows*n_col - 1
        while l <= r:
            m = (l+r)//2
            i = m // n_col
            j = m % n_col
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                r = m - 1
            else:
                l = m + 1
        return False