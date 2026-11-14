from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_pos_sum = float('inf')
        
        # Iterate over all possible starting indices
        for i in range(n):
            current_sum = 0
            
            # Expand the subarray up to the maximum allowed length `r`
            for j in range(i, min(i + r, n)):
                current_sum += nums[j]
                
                # Check if the current length is within the valid range
                length = j - i + 1
                if length >= l and current_sum > 0:
                    if current_sum < min_pos_sum:
                        min_pos_sum = current_sum
                        
        return int(min_pos_sum) if min_pos_sum != float('inf') else -1