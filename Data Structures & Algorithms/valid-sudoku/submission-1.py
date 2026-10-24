class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        for r, row in enumerate(board):
            for c, value in enumerate(row):
                if value != ".":
                    if value in rows[r] or value in cols[c] or value in squares[r // 3][c // 3]:
                        return False
                    rows[r].add(value)
                    cols[c].add(value)
                    squares[r // 3][c // 3].add(value)
        return True