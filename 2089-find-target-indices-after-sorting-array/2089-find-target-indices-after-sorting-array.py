class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # 1. Sort the array
        nums.sort()
        
        # 2. Find all indices where the element equals the target
        result = []
        for i, num in enumerate(nums):
            if num == target:
                result.append(i)
                
        return result