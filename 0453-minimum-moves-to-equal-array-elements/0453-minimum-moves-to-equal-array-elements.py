from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Find the minimum element in the array
        min_val = min(nums)
        
        # Calculate the total moves required
        return sum(nums) - len(nums) * min_val