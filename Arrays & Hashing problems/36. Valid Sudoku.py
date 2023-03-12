#https://leetcode.com/problems/valid-sudoku/description/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [0 for _ in range(9)]
        for i in range(9):
            row = 0
            if i%3 == 0:
                cells = [0 for _ in range(3)] 
            for j in range(9):
                if board[i][j] == ".":
                    continue
                pos = 1 << (int(board[i][j])-1)
                if pos & row:
                    return False
                row |= pos
                if pos & columns[j]:
                    return False
                columns[j] |= pos
                if pos & cells[j//3]:
                    return False
                cells[j//3] |= pos
        return True