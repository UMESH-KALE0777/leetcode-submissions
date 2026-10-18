class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute Pascal's triangle for combinations
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def count_ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            n_left, n_right = len(left), len(right)
            
            left_ways = count_ways(left)
            right_ways = count_ways(right)
            
            return (comb[n_left + n_right][n_left] * left_ways % MOD * right_ways) % MOD

        return (count_ways(nums) - 1 + MOD) % MOD