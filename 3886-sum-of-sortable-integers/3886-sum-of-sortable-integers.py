class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        pref_max = [0] * n
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i-1], nums[i])
            
        suff_min = [0] * n
        suff_min[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suff_min[i] = min(suff_min[i+1], nums[i])
            
        descents = [0] * n
        for i in range(n - 1):
            descents[i+1] = descents[i] + (1 if nums[i] > nums[i+1] else 0)
            
        ans = 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            
            is_valid = True
            for i in range(n // k):
                L = i * k
                R = L + k - 1
                
                if R < n - 1 and pref_max[R] > suff_min[R+1]:
                    is_valid = False
                    break
                    
                c = descents[R] - descents[L]
                if c > 1 or (c == 1 and nums[R] > nums[L]):
                    is_valid = False
                    break
                    
            if is_valid:
                ans += k
                
        return ans