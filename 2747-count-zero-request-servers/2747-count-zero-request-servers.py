from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time
        logs.sort(key=lambda item: item[1])
        
        # Keep track of original query indices to place answers in the correct order
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        ans = [0] * len(queries)
        counts = [0] * (n + 1)
        
        left = 0
        right = 0
        active_servers = 0
        
        for q, original_idx in sorted_queries:
            # 1. Expand the window to include logs up to the end of the query interval 'q'
            while right < len(logs) and logs[right][1] <= q:
                server_id = logs[right][0]
                if counts[server_id] == 0:
                    active_servers += 1
                counts[server_id] += 1
                right += 1
                
            # 2. Shrink the window to remove logs before the start of the query interval 'q - x'
            while left < len(logs) and logs[left][1] < q - x:
                server_id = logs[left][0]
                counts[server_id] -= 1
                if counts[server_id] == 0:
                    active_servers -= 1
                left += 1
                
            # 3. Calculate servers with zero requests
            ans[original_idx] = n - active_servers
            
        return ans