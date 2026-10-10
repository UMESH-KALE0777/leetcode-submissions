class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        # Calculate the absolute difference for each pair
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        k = k1 + k2
        total_diff = sum(diffs)
        
        # If we have enough operations to reduce all differences to 0
        if k >= total_diff:
            return 0
            
        # The maximum possible difference is 10^5 based on constraints
        max_diff = max(diffs)
        counts = [0] * (max_diff + 1)
        
        # Count frequencies of each difference
        for diff in diffs:
            counts[diff] += 1
            
        # Greedily reduce the largest differences first
        for i in range(max_diff, 0, -1):
            if counts[i] > 0:
                # We can reduce at most `counts[i]` items, or `k` items, whichever is smaller
                reduce_amount = min(counts[i], k)
                
                counts[i] -= reduce_amount
                counts[i - 1] += reduce_amount
                k -= reduce_amount
                
                # If we run out of operations, stop
                if k == 0:
                    break
                    
        # Calculate the final sum of squared differences
        ans = 0
        for i in range(1, max_diff + 1):
            if counts[i] > 0:
                ans += counts[i] * i * i
                
        return ans