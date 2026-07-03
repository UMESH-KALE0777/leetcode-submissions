from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        # Keep only edges whose endpoints are both online
        filtered = [(u, v, c) for u, v, c in edges if online[u] and online[v]]
        if not filtered:
            return -1

        # Build adjacency list + indegree for topological sort
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v, c in filtered:
            adj[u].append((v, c))
            indeg[v] += 1

        order = []
        q = deque(i for i in range(n) if indeg[i] == 0)
        while q:
            u = q.popleft()
            order.append(u)
            for v, c in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        costs = sorted(set(c for _, _, c in filtered))

        INF = float('inf')

        def feasible(T: int) -> bool:
            dp = [INF] * n
            dp[0] = 0
            for u in order:
                if dp[u] == INF:
                    continue
                du = dp[u]
                for v, c in adj[u]:
                    if c >= T and du + c < dp[v]:
                        dp[v] = du + c
            return dp[n - 1] <= k

        lo, hi, ans = 0, len(costs) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans