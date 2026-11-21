import sys
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        # Increase recursion depth to handle highly degenerate trees (e.g., linked-list shape)
        sys.setrecursionlimit(200005)
        n = len(parent)
        
        # 1. Build original tree adjacency list
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = [-1] * 26
        
        # 2. Find new parents using DFS on the original tree
        def find_new_parents(node: int):
            char_idx = ord(s[node]) - ord('a')
            prev_ancestor = last_seen[char_idx]
            
            # If an ancestor with the same character exists, re-wire the parent
            if prev_ancestor != -1:
                new_parent[node] = prev_ancestor
                
            # Update the state for the descendants
            last_seen[char_idx] = node
            
            for child in adj[node]:
                find_new_parents(child)
                
            # Backtrack to restore state for parallel branches
            last_seen[char_idx] = prev_ancestor

        find_new_parents(0)
        
        # 3. Build the new tree adjacency list
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        
        # 4. Calculate subtree sizes on the newly formed tree
        def calc_sizes(node: int):
            for child in new_adj[node]:
                calc_sizes(child)
                ans[node] += ans[child]
                
        calc_sizes(0)
        
        return ans