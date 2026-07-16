import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        
        # Step 1: Construct the prefixGcd array
        current_max = 0
        for num in nums:
            current_max = max(current_max, num)
            prefixGcd.append(math.gcd(num, current_max))
            
        # Step 2: Sort prefixGcd in non-decreasing order
        prefixGcd.sort()
        
        # Step 3 & 4: Form pairs using two pointers
        # Combine the smallest unpaired (left) and largest unpaired (right) elements
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        # If n is odd, the middle element is left at left == right, 
        # which is automatically ignored since our loop condition is strict (left < right).
        
        return total_sum