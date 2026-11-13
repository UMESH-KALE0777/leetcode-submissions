from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Prefix sum of nums to easily query sum(nums[L...R]) in O(1) time
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
            
        # Monotonic stack stores tuples of: 
        # (start_index, max_value_in_block, cumulative_P_sum_to_the_end_of_array)
        # We place a sentinel at the bottom representing the out-of-bounds boundary
        st = [(n, 0, 0)]
        
        def get_suffix_P(idx):
            """Returns the sum of prefix maximums from `idx` to n - 1."""
            if idx >= n:
                return 0
            
            # Binary search to find the block containing `idx`
            low, high = 0, len(st) - 1
            j = -1
            while low <= high:
                mid = (low + high) // 2
                if st[mid][0] <= idx:
                    j = mid
                    high = mid - 1  # Try to find a block further left in the stack (higher index)
                else:
                    low = mid + 1
                    
            # The block `j` starts at st[j][0] and goes up to st[j-1][0] - 1
            partial_len = st[j - 1][0] - idx
            return partial_len * st[j][1] + st[j - 1][2]
            
        ans = 0
        R = n - 1
        
        # Traverse the left boundary L backwards
        for L in range(n - 1, -1, -1):
            val = nums[L]
            
            # Maintain the monotonic decreasing property of the stack
            while len(st) > 1 and st[-1][1] <= val:
                st.pop()
                
            # Create a new block extending from L to the start of the next block
            length = st[-1][0] - L
            cum = st[-1][2] + length * val
            st.append((L, val, cum))
            
            # Two-pointer: Shrink the right boundary R until the cost is <= k
            while R >= L:
                total_P = st[-1][2] - get_suffix_P(R + 1)
                total_nums = pref[R + 1] - pref[L]
                
                if total_P - total_nums > k:
                    R -= 1
                else:
                    break
                    
            # All subarrays starting at L and ending anywhere up to R are valid
            ans += (R - L + 1)
            
        return ans