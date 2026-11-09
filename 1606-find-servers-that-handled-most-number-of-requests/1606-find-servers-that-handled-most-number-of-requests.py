import heapq
from typing import List
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Count of requests handled by each server
        request_count = [0] * k
        
        # Min-heap to store busy servers: (finish_time, server_id)
        busy = []
        
        # SortedList to store IDs of currently available servers
        available = SortedList(range(k))
        
        for i, (arr, l) in enumerate(zip(arrival, load)):
            # 1. Release all servers that have finished before or at arrival[i]
            while busy and busy[0][0] <= arr:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
                
            # If no servers are available, drop the request
            if not available:
                continue
                
            # 2. Find the first available server >= (i % k)
            target = i % k
            idx = available.bisect_left(target)
            
            # If wrap around is needed
            if idx == len(available):
                idx = 0
                
            assigned_server = available[idx]
            
            # 3. Assign request to the chosen server
            available.remove(assigned_server)
            heapq.heappush(busy, (arr + l, assigned_server))
            request_count[assigned_server] += 1
            
        # 4. Find all servers that handled the maximum number of requests
        max_requests = max(request_count)
        return [i for i in range(k) if request_count[i] == max_requests]