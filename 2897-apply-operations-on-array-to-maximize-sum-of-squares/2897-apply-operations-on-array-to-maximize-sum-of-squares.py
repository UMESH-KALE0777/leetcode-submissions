class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Count the occurrences of each bit position
        bit_counts = [0] * 32
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
        
        ans = 0
        
        # Step 2: Greedily build the k largest numbers possible
        for _ in range(k):
            current_num = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            
            # Step 3: Accumulate the square modulo 10^9 + 7
            ans = (ans + current_num * current_num) % MOD
            
        return ans