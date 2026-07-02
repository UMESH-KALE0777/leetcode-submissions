from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        inf = float('inf')
        cost = [[inf] * n for _ in range(m)]
        
        dq = deque()
        
        start_cost = grid[0][0]
        cost[0][0] = start_cost
        dq.append((0, 0))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while dq:
            r, c = dq.popleft()
            
            if r == m - 1 and c == n - 1:
                break
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    next_cost = cost[r][c] + grid[nr][nc]
                    
                    if next_cost < cost[nr][nc]:
                        cost[nr][nc] = next_cost
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
        
        return cost[m - 1][n - 1] < health