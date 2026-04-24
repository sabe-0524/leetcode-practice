from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0] * col for _ in range(row)]
        for i in range(col):
            dp[0][i] = 1 if obstacleGrid[0][i] == 0 and (i == 0 or dp[0][i - 1] == 1) else 0
        for i in range(row):
            dp[i][0] = 1 if obstacleGrid[i][0] == 0 and (i == 0 or dp[i - 1][0] == 1)else 0
        
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        return dp[row - 1][col - 1]