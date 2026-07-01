from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        dist_to_thief = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist_to_thief[r][c] = 0
                    queue.append((r, c))
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist_to_thief[nr][nc] == float('inf'):
                    dist_to_thief[nr][nc] = dist_to_thief[r][c] + 1
                    queue.append((nr, nc))
                    
        max_heap = [(-dist_to_thief[0][0], 0, 0)]
        max_safeness = [[-1] * n for _ in range(n)]
        max_safeness[0][0] = dist_to_thief[0][0]
        
        while max_heap:
            safe, r, c = heapq.heappop(max_heap)
            safe = -safe  
            
            if r == n - 1 and c == n - 1:
                return safe
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    next_safe = min(safe, dist_to_thief[nr][nc])
                    
                    if next_safe > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = next_safe
                        heapq.heappush(max_heap, (-next_safe, nr, nc))
                        
        return 0