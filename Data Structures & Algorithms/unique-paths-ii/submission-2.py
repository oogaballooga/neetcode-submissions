class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                    continue
                
                if r == ROWS-1 and c == COLS-1:
                    obstacleGrid[r][c] = 1
                
                if r + 1 < ROWS:
                    obstacleGrid[r][c] += obstacleGrid[r+1][c]
                
                if c + 1 < COLS:
                    obstacleGrid[r][c] += obstacleGrid[r][c+1]
                
        return obstacleGrid[0][0]