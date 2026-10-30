import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Priority queue stores tuples of (distance, current_node, current_streak)
        pq = [(0, 0, 1)]
        
        # min_c[u] stores the smallest streak of consecutive characters we've seen so far for node u
        # Initialized to k + 1 because we only care about streaks <= k
        min_c = [k + 1] * n
        
        while pq:
            d, u, c = heapq.heappop(pq)
            
            # If we reached the target node, since Dijkstra guarantees shortest distance first, return d
            if u == n - 1:
                return d
                
            # If we have already visited this node with a smaller or equal streak, skip it
            if c >= min_c[u]:
                continue
                
            # Update the minimum streak for node u
            min_c[u] = c
            
            # Traverse neighbors
            for v, w in adj[u]:
                if labels[u] == labels[v]:
                    next_c = c + 1
                else:
                    next_c = 1
                    
                # If the transition is valid (streak doesn't exceed k), push to the priority queue
                if next_c <= k:
                    heapq.heappush(pq, (d + w, v, next_c))
                    
        return -1