from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp_0, dp_1, dp_2 represent the minimum costs to reach 
        # step i-3, step i-2, and step i-1 respectively.
        # Initially, we start at step 0, so dp_2 (step 0) is 0. 
        # dp_1 and dp_0 are infinitely large as they represent out-of-bounds steps.
        dp_0, dp_1, dp_2 = float('inf'), float('inf'), 0
        
        for i in range(1, n + 1):
            step_cost = costs[i - 1]
            
            # Minimum cost to jump to the current step i
            min_jump_cost = dp_2 + 1
            if i >= 2:
                min_jump_cost = min(min_jump_cost, dp_1 + 4)
            if i >= 3:
                min_jump_cost = min(min_jump_cost, dp_0 + 9)
                
            # Total cost to land on step i
            curr_cost = min_jump_cost + step_cost
            
            # Shift the window of our 3 previous steps forward
            dp_0, dp_1, dp_2 = dp_1, dp_2, curr_cost
            
        return dp_2