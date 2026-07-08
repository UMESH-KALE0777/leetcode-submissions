class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        # Extract non-zero digits and their original indices
        nz_digits = []
        nz_indices = []
        for i, ch in enumerate(s):
            if ch != '0':
                nz_digits.append(int(ch))
                nz_indices.append(i)
                
        n = len(nz_digits)
        if n == 0:
            return [0] * len(queries)
            
        # Precompute next_nz and prev_nz mappings
        next_nz = [n] * m
        prev_nz = [-1] * m
        
        # Fill next_nz
        curr = n
        for i in range(m - 1, -1, -1):
            if s[i] != '0':
                # Find the index in nz_indices
                # Since we iterate backward, we can track it or use a pointer
                pass
        
        # A cleaner way to fill mappings:
        nz_ptr = 0
        for i in range(m):
            if nz_ptr < n and nz_indices[nz_ptr] < i:
                nz_ptr += 1
            next_nz[i] = nz_ptr
            
        nz_ptr = n - 1
        for i in range(m - 1, -1, -1):
            if nz_ptr >= 0 and nz_indices[nz_ptr] > i:
                nz_ptr -= 1
            prev_nz[i] = nz_ptr
            
        # Precompute prefix sums, prefix values, and powers of 10
        pref_sum = [0] * (n + 1)
        pref_val = [0] * (n + 1)
        pow10 = [1] * (n + 1)
        
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + nz_digits[i]
            pref_val[i + 1] = (pref_val[i] * 10 + nz_digits[i]) % MOD
            pow10[i + 1] = (pow10[i] * 10) % MOD
            
        ans = []
        for l, r in queries:
            # Map string indices to compressed non-zero indices
            q_l = next_nz[l]
            q_r = prev_nz[r]
            
            if q_l > q_r:
                ans.append(0)
                continue
                
            # Get digit sum
            digit_sum = pref_sum[q_r + 1] - pref_sum[q_l]
            
            # Get substring numeric value x % MOD
            length = q_r - q_l + 1
            x = (pref_val[q_r + 1] - pref_val[q_l] * pow10[length]) % MOD
            
            # Compute result
            ans.append((x * digit_sum) % MOD)
            
        return ans