from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Find the maximum element, which is our target value
        max_val = max(nums)
        
        # Calculate the minimum total moves to reach max_val
        return max_val * len(nums) - sum(nums)