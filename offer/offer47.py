# author: tobebetter9527
# since: 2023/5/19 17:52
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + grid[row][0]
        for col in range(1, n):
            dp[0][col] = dp[0][col - 1] + grid[0][col]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = max(dp[row - 1][col] + grid[row][col], dp[row][col - 1] + grid[row][col])
        return dp[m - 1][n - 1]
