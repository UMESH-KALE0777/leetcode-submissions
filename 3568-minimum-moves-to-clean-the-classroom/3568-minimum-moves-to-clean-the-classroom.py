from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        sx = sy = -1
        litter_pos = {}
        litter_idx = 0
        
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    litter_pos[(i, j)] = litter_idx
                    litter_idx += 1
                    
        target_mask = (1 << litter_idx) - 1
        if target_mask == 0:
            return 0
            
        best_energy = [[[-1] * (1 << litter_idx) for _ in range(n)] for _ in range(m)]
        
        q = deque([(sx, sy, 0, energy)])
        best_energy[sx][sy][0] = energy
        steps = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            for _ in range(len(q)):
                x, y, mask, e = q.popleft()
                
                if mask == target_mask:
                    return steps
                    
                if e > 0:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        
                        if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                            nxt_e = e - 1
                            nxt_mask = mask
                            
                            cell = classroom[nx][ny]
                            if cell == 'R':
                                nxt_e = energy
                            elif cell == 'L':
                                nxt_mask |= (1 << litter_pos[(nx, ny)])
                                
                            if nxt_e > best_energy[nx][ny][nxt_mask]:
                                best_energy[nx][ny][nxt_mask] = nxt_e
                                q.append((nx, ny, nxt_mask, nxt_e))
            steps += 1
            
        return -1