from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sort the array to easily find the median
        nums.sort()
        
        # Find the median value
        median = nums[len(nums) // 2]
        
        # Sum the absolute differences from the median
        return sum(abs(num - median) for num in nums)