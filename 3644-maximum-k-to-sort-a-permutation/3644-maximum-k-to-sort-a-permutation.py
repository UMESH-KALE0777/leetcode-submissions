class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = -1
        
        for i, x in enumerate(nums):
            if x != i:
                if ans == -1:
                    ans = x
                else:
                    ans &= x
                    
        return ans if ans != -1 else 0