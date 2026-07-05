from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        
       
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        
        dp[0][0] = [0, 1]
        
        
        for r in range(n):
            for c in range(n):
                
                if board[r][c] == 'X' or (r == 0 and c == 0):
                    continue
                
                max_prev_score = -1
                total_paths = 0
                
                
                for dr, dc in [(-1, 0), (0, -1), (-1, -1)]:
                    prev_r, prev_c = r + dr, c + dc
                    
                    if 0 <= prev_r < n and 0 <= prev_c < n:
                        prev_score, prev_paths = dp[prev_r][prev_c]
                        
                       
                        if prev_score != -1:
                            if prev_score > max_prev_score:
                                max_prev_score = prev_score
                                total_paths = prev_paths
                            elif prev_score == max_prev_score:
                                total_paths = (total_paths + prev_paths) % MOD
                
               
                if max_prev_score != -1:
                    current_val = int(board[r][c]) if board[r][c] != 'S' else 0
                    dp[r][c] = [max_prev_score + current_val, total_paths]
        
        
        final_score, final_paths = dp[n-1][n-1]
        
        return [final_score, final_paths] if final_score != -1 else [0, 0]