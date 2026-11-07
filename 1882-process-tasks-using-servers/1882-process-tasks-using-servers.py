import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Initialize free_servers with (weight, index)
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        busy_servers = []  # Stores tuples of (free_time, weight, index)
        ans = []
        
        current_time = 0
        
        for j, duration in enumerate(tasks):
            # Advance time normally to the arrival of the j-th task, 
            # ensuring time never moves backward.
            current_time = max(current_time, j)
            
            # 1. Release all servers that have finished processing by `current_time`
            while busy_servers and busy_servers[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
            
            # 2. Fast-forward time if no servers are currently free
            if not free_servers:
                current_time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= current_time:
                    free_time, weight, index = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (weight, index))
                    
            # 3. Assign the task to the best available free server
            weight, index = heapq.heappop(free_servers)
            ans.append(index)
            
            # 4. Mark the server as busy until it finishes this new task
            heapq.heappush(busy_servers, (current_time + duration, weight, index))
            
        return ans