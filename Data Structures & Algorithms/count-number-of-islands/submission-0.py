class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def search(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0" or grid[r][c] == "#"):
                return
            
            grid[r][c] = "#"
            search(r+1, c)
            search(r-1, c)
            search(r, c+1)
            search(r, c-1)
            return 1

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += search(r, c)
        
        return islands