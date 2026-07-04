from collections import deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build the adjacency list
        # We store tuples of (neighbor, distance)
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: BFS to traverse the connected component containing node 1
        min_score = float('inf')
        visited = set()
        queue = deque([1])
        visited.add(1)
        
        while queue:
            node = queue.popleft()
            
            for neighbor, weight in graph[node]:
                # Update the minimum score with every edge we can reach
                min_score = min(min_score, weight)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score