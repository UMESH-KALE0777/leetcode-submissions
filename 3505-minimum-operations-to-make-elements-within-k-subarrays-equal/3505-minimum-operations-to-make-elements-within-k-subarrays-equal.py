import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        costs = []
        
        # Max-heap for the smaller half: stores (-value, -index)
        left_heap = []
        # Min-heap for the larger half: stores (value, index)
        right_heap = []
        
        left_sum = 0
        right_sum = 0
        left_count = 0
        right_count = 0
        
        # Track explicitly which heap each element belongs to by its exact index
        in_left = [False] * n
        # Track elements that have fallen out of the window by index
        removed = set()
        
        def clean_left():
            while left_heap and -left_heap[0][1] in removed:
                heapq.heappop(left_heap)
                
        def clean_right():
            while right_heap and right_heap[0][1] in removed:
                heapq.heappop(right_heap)

        for i in range(n):
            val = nums[i]
            
            # 1. Insert the new element
            clean_left()
            if left_count == 0 or val <= -left_heap[0][0]:
                heapq.heappush(left_heap, (-val, -i))
                left_sum += val
                left_count += 1
                in_left[i] = True
            else:
                heapq.heappush(right_heap, (val, i))
                right_sum += val
                right_count += 1
                in_left[i] = False
                
            # 2. Remove the element that slid out of the window logically
            if i >= x:
                out_idx = i - x
                out_val = nums[out_idx]
                removed.add(out_idx)
                
                # We know exactly which heap to deduct from using in_left
                if in_left[out_idx]:
                    left_sum -= out_val
                    left_count -= 1
                else:
                    right_sum -= out_val
                    right_count -= 1
                    
            # 3. Rebalance the heaps based on valid logical counts
            curr_size = min(i + 1, x)
            target_left = (curr_size + 1) // 2
            
            while left_count > target_left:
                clean_left()
                neg_val, neg_idx = heapq.heappop(left_heap)
                moved_val = -neg_val
                moved_idx = -neg_idx
                
                left_sum -= moved_val
                left_count -= 1
                in_left[moved_idx] = False
                
                heapq.heappush(right_heap, (moved_val, moved_idx))
                right_sum += moved_val
                right_count += 1
                
            while left_count < target_left:
                clean_right()
                moved_val, moved_idx = heapq.heappop(right_heap)
                
                right_sum -= moved_val
                right_count -= 1
                in_left[moved_idx] = True
                
                heapq.heappush(left_heap, (-moved_val, -moved_idx))
                left_sum += moved_val
                left_count += 1
                
            # 4. Record the precomputed minimum operational cost for this window
            if i >= x - 1:
                clean_left()
                median = -left_heap[0][0]
                cost = right_sum - left_sum + (median * (left_count - right_count))
                costs.append(cost)
                
        # 5. Dynamic Programming to find the minimum cost for `k` non-overlapping subarrays
        prev_dp = [0] * (n + 1)
        
        for j in range(1, k + 1):
            curr_dp = [float('inf')] * (n + 1)
            # We can only form `j` subarrays if we have at least `j * x` elements available
            start_index = x * j
            for idx in range(start_index, n + 1):
                # We either skip the current element or pick the newly formed subarray
                skip_cost = curr_dp[idx - 1]
                pick_cost = prev_dp[idx - x] + costs[idx - x]
                curr_dp[idx] = min(skip_cost, pick_cost)
                
            prev_dp = curr_dp
            
        return int(prev_dp[n])