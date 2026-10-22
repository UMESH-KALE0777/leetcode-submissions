class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        zero = nums.index(0)
        
        def check(step: int) -> bool:
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n
                if nums[prev] > nums[curr]:
                    return False
            return True

        ans = float('inf')

        # Forward cyclic shift
        if check(1):
            ans = min(ans, zero, n - zero + 2)

        # Reversed cyclic shift
        if check(-1):
            ans = min(ans, zero + 2, n - zero)

        return ans if ans != float('inf') else -1