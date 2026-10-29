from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        in_time = [0] * n
        out_time = [0] * n
        depth = [0] * n
        parent = [0] * n
        
        # Iterative DFS for Euler tour to prevent RecursionError on deep trees
        timer = 0
        stack = [0]
        visited = [False] * n
        
        while stack:
            u = stack[-1]
            if not visited[u]:
                visited[u] = True
                timer += 1
                in_time[u] = timer
                for v in adj[u]:
                    if not visited[v]:  # V is a child
                        parent[v] = u
                        depth[v] = depth[u] + 1
                        stack.append(v)
            else:
                out_time[u] = timer
                stack.pop()
                
        # BFS order to populate Binary Lifting table top-down
        up = [[0] * 16 for _ in range(n)]
        bfs = [0]
        for u in bfs:
            for v in adj[u]:
                if v != parent[u]:
                    bfs.append(v)
                    
        for u in bfs:
            up[u][0] = parent[u]
            for i in range(1, 16):
                up[u][i] = up[up[u][i-1]][i-1]
                
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(16):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(15, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]
        
        # Fenwick Tree (Binary Indexed Tree) for range XOR updates and point queries
        bit = [0] * (n + 2)
        
        def add(idx: int, val: int):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        # Initialize the state of characters and the Fenwick tree
        s_arr = [ord(c) - 97 for c in s]
        for i in range(n):
            val = 1 << s_arr[i]
            add(in_time[i], val)
            add(out_time[i] + 1, val)
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = ord(parts[2]) - 97
                diff = (1 << s_arr[u]) ^ (1 << c)
                
                # Apply range XOR update on the subtree of 'u'
                add(in_time[u], diff)
                add(out_time[u] + 1, diff)
                s_arr[u] = c
                
            else:
                u, v = int(parts[1]), int(parts[2])
                lca = get_lca(u, v)
                
                # P(u) ^ P(v) ^ char(LCA)
                path_xor = query(in_time[u]) ^ query(in_time[v]) ^ (1 << s_arr[lca])
                
                # Checks if it has at most 1 bit set to `1` (Valid Palindrome Anagram logic)
                ans.append(path_xor == 0 or (path_xor & (path_xor - 1)) == 0)
                
        return ans