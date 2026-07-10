from bisect import bisect_right
from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 1. Pair each node with its original index and sort by value
        sorted_nodes = sorted([(nums[i], i) for i in range(n)])
        
        # Map original index back to its sorted position
        pos_in_sorted = [0] * n
        for sorted_idx, (val, orig_idx) in enumerate(sorted_nodes):
            pos_in_sorted[orig_idx] = sorted_idx
            
        # 2. Compute the immediate greedy parent for each sorted node
        # parent[i] stores the index of the furthest node reachable from sorted_nodes[i]
        LOG = 18  # Since n <= 10^5, 2^17 = 131,072 > 10^5
        up = [[i] * LOG for i in range(n)]
        
        for i in range(n):
            curr_val = sorted_nodes[i][0]
            # Find the furthest node to the right within maxDiff
            # We look for the first element strictly greater than curr_val + maxDiff
            target_val = curr_val + maxDiff
            # Binary search over the values array
            idx = bisect_right(sorted_nodes, (target_val, float('inf'))) - 1
            
            # If the furthest reachable node is ahead of us, set it as our next jump
            if idx > i:
                up[i][0] = idx
            else:
                up[i][0] = i  # Cannot move forward
                
        # 3. Build the binary lifting table
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # 4. Process each query
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            p_u = pos_in_sorted[u]
            p_v = pos_in_sorted[v]
            
            # Ensure p_u is always the smaller value node (moving towards larger p_v)
            if p_u > p_v:
                p_u, p_v = p_v, p_u
                
            # Count the total jumps needed to reach or pass p_v
            steps = 0
            curr = p_u
            
            # Try to make large jumps without overshooting p_v
            for j in range(LOG - 1, -1, -1):
                if up[curr][j] < p_v:
                    curr = up[curr][j]
                    steps += (1 << j)
            
            # After the loop, curr is the furthest node we can reach that is strictly less than p_v
            # Take one final step to see if we can reach or overshoot p_v
            final_jump = up[curr][0]
            if final_jump >= p_v and sorted_nodes[curr][0] + maxDiff >= sorted_nodes[p_v][0]:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans