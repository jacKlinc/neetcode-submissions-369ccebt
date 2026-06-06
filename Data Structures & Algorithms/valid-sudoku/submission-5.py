class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = []
        cube_ctr = 0
        for i in range(9):
            row = board[i]
            # check row is unique
            unique_chars = [r for r in row if r != "."]
            if len(set(unique_chars)) != len(unique_chars):
                return False
            # check col is unique
            col = [board[j][i] for j in range(9) if board[j][i] != "."]
            if len(set(col)) != len(col):
                return False

            # check all squares in the grid
            row_start = (i // 3) * 3
            col_start = (i % 3) * 3
            square = []
            for r in range(row_start, row_start + 3):
                for c in range(col_start, col_start + 3):
                    if board[r][c] != ".":
                        square.append(board[r][c])
                        
            if len(square) != len(set(square)):
                return False

        return True