from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        
        # Option 1: Drop the two smallest elements
        opt1 = nums[-1] - nums[2]
        
        # Option 2: Drop the smallest and the largest element
        opt2 = nums[-2] - nums[1]
        
        # Option 3: Drop the two largest elements
        opt3 = nums[-3] - nums[0]
        
        # Return the minimum possible high score (low score is always 0)
        return min(opt1, opt2, opt3)