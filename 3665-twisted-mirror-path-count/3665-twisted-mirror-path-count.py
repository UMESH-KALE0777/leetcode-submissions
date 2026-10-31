from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        # We flatten the 2D arrays into 1D for memory efficiency and faster lookups.
        # -1 means the robot goes out of bounds.
        jumpR = [-1] * (m * n)
        jumpD = [-1] * (m * n)
        
        # 1. Precompute destinations from bottom-right to top-left
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                idx = r * n + c
                if grid[r][c] == 0:
                    # Empty cell: stops immediately
                    jumpR[idx] = idx
                    jumpD[idx] = idx
                else:
                    # Mirror cell: reflects
                    
                    # Entered moving Right -> Turns Down
                    if r + 1 < m:
                        jumpR[idx] = jumpD[(r + 1) * n + c]
                        
                    # Entered moving Down -> Turns Right
                    if c + 1 < n:
                        jumpD[idx] = jumpR[r * n + c + 1]
                        
        # 2. Dynamic Programming to count paths
        dp = [0] * (m * n)
        dp[0] = 1  # 1 way to be at the start
        
        # Traverse in topological order (row by row, left to right)
        for r in range(m):
            for c in range(n):
                idx = r * n + c
                
                # If cell is unreachable or is a mirror, we don't branch from it
                if dp[idx] == 0 or grid[r][c] == 1:
                    continue
                    
                # Option 1: Move Right
                if c + 1 < n:
                    dest = jumpR[r * n + c + 1]
                    if dest != -1:
                        dp[dest] = (dp[dest] + dp[idx]) % MOD
                        
                # Option 2: Move Down
                if r + 1 < m:
                    dest = jumpD[(r + 1) * n + c]
                    if dest != -1:
                        dp[dest] = (dp[dest] + dp[idx]) % MOD
                        
        return dp[(m - 1) * n + n - 1]