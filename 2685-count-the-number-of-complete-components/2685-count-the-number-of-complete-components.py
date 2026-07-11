from collections import deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        complete_components_count = 0
        
        # Step 2: Traverse the graph
        for i in range(n):
            if not visited[i]:
                # Start BFS for a new component
                queue = deque([i])
                visited[i] = True
                
                component_nodes = 0
                component_edges = 0
                
                while queue:
                    curr = queue.popleft()
                    component_nodes += 1
                    # Count the degrees of all nodes in this component
                    component_edges += len(adj[curr])
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # In an undirected graph, each edge is counted twice (once from each endpoint)
                # So the condition: total_edges == V * (V - 1)
                if component_edges == component_nodes * (component_nodes - 1):
                    complete_components_count += 1
                    
        return complete_components_count