class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        valid_islands = 0
        
        def dfs(r: int, c: int) -> int:
            # Base condition: out of bounds or water/visited cell
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            # Save cell value and mark as visited in-place
            val = grid[r][c]
            grid[r][c] = 0
            
            # Explore all 4 adjacent directions
            val += dfs(r + 1, c)
            val += dfs(r - 1, c)
            val += dfs(r, c + 1)
            val += dfs(r, c - 1)
            
            return val

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    island_sum = dfs(r, c)
                    if island_sum % k == 0:
                        valid_islands += 1
                        
        return valid_islands