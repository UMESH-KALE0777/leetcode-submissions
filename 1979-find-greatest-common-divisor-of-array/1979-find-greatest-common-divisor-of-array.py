class Solution:
    def findGCD(self, nums: list[int]) -> int:
        # Find the minimum and maximum elements in the array
        mn = min(nums)
        mx = max(nums)
        
        # Euclidean Algorithm to find GCD
        while mn:
            mx, mn = mn, mx % mn
            
        return mx