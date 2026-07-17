import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Step 1: Count frequency of each number
        count = [0] * (max_val + 1)
        for num in nums:
            count[num] += 1
            
        # gcd_count[g] will store the exact number of pairs with GCD equal to g
        gcd_count = [0] * (max_val + 1)
        
        # Step 2 & 4: Process from max_val down to 1 (Inclusion-Exclusion)
        for g in range(max_val, 0, -1):
            # Count elements divisible by g
            divisible_count = 0
            for multiple in range(g, max_val + 1, g):
                divisible_count += count[multiple]
                
            # Total pairs that share g as a common divisor
            total_pairs = (divisible_count * (divisible_count - 1)) // 2
            
            # Subtract pairs that have a strictly larger common multiple as their actual GCD
            minus_pairs = 0
            for multiple in range(2 * g, max_val + 1, g):
                minus_pairs += gcd_count[multiple]
                
            gcd_count[g] = total_pairs - minus_pairs
            
        # Step 5: Build a prefix sum array to map indices to GCD values
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_count[i]
            
        # Answer each query using binary search
        ans = []
        for q in queries:
            # We look for the first index where prefix_sums[idx] > q
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans