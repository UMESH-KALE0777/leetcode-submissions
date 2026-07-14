import math

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        
        # dp[g1][g2] stores the number of pairs of subsequences 
        # with GCD g1 and g2 respectively. 0 means empty.
        dp = {}
        dp[(0, 0)] = 1
        
        for x in nums:
            next_dp = dp.copy()
            
            for (g1, g2), count in dp.items():
                # Choice 1: Add x to the first subsequence
                ng1 = math.gcd(g1, x) if g1 != 0 else x
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD
                
                # Choice 2: Add x to the second subsequence
                ng2 = math.gcd(g2, x) if g2 != 0 else x
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD
                
            dp = next_dp
            
        ans = 0
        # Sum up all configurations where both subsequences are non-empty and have equal GCD
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans