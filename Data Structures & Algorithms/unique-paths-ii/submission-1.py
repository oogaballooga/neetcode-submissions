class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    continue
                
                if r == ROWS-1 and c == COLS-1:
                    dp[r][c] = 1
                
                if r + 1 < ROWS:
                    dp[r][c] += dp[r+1][c]
                
                if c + 1 < COLS:
                    dp[r][c] += dp[r][c+1]
                
        return dp[0][0]