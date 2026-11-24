import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 2  # Any subarray of length 2 satisfies prod == lcm * gcd
        
        for i in range(n):
            curr_prod = nums[i]
            curr_gcd = nums[i]
            curr_lcm = nums[i]
            
            for j in range(i + 1, n):
                curr_prod *= nums[j]
                curr_gcd = math.gcd(curr_gcd, nums[j])
                curr_lcm = math.lcm(curr_lcm, nums[j])
                
                if curr_prod == curr_lcm * curr_gcd:
                    max_len = max(max_len, j - i + 1)
                elif curr_prod > curr_lcm * curr_gcd:
                    # Product grows at least as fast as lcm * gcd; it can never equalize again
                    break
                    
        return max_len