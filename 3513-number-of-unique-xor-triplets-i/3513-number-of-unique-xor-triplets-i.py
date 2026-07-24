class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Handle the base cases separately
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # For n >= 3, all numbers up to the next power of 2 are possible
        return 1 << n.bit_length()