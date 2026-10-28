from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] will store all possible XOR sums to reach cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Base case: starting cell
        dp[0][0].add(grid[0][0])
        
        for i in range(m):
            for j in range(n):
                # If we can move down from (i-1, j)
                if i > 0:
                    for val in dp[i-1][j]:
                        dp[i][j].add(val ^ grid[i][j])
                
                # If we can move right from (i, j-1)
                if j > 0:
                    for val in dp[i][j-1]:
                        dp[i][j].add(val ^ grid[i][j])
                        
        # The answer is the minimum XOR sum to reach the bottom-right cell
        return min(dp[m-1][n-1])