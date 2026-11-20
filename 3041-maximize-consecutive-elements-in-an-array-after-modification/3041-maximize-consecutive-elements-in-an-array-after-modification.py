from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        
        for x in nums:
            # Calculate new lengths before updating to prevent the same 
            # element from chaining with itself in a single step
            inc_length = dp.get(x, 0) + 1
            keep_length = dp.get(x - 1, 0) + 1
            
            # Update the DP map with the new lengths
            dp[x + 1] = inc_length
            dp[x] = keep_length
            
        return max(dp.values())