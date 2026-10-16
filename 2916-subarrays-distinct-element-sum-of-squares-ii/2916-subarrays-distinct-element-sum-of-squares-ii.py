class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        sum_sq = [0] * (4 * n)
        sum_val = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def apply(node: int, l: int, r: int, val: int):
            length = r - l + 1
            # (A+v)^2 = A^2 + 2vA + v^2
            sum_sq[node] = (sum_sq[node] + 2 * val * sum_val[node] + val * val * length) % MOD
            sum_val[node] = (sum_val[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD
            
        def push_down(node: int, l: int, r: int):
            if lazy[node] != 0:
                mid = (l + r) // 2
                apply(node * 2, l, mid, lazy[node])
                apply(node * 2 + 1, mid + 1, r, lazy[node])
                lazy[node] = 0
                
        def update(node: int, l: int, r: int, ql: int, qr: int, val: int):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)
            
            sum_val[node] = (sum_val[node * 2] + sum_val[node * 2 + 1]) % MOD
            sum_sq[node] = (sum_sq[node * 2] + sum_sq[node * 2 + 1]) % MOD

        ans = 0
        last_pos = {}
        
        for i, x in enumerate(nums):
            start = last_pos.get(x, -1) + 1
            update(1, 0, n - 1, start, i, 1)
            ans = (ans + sum_sq[1]) % MOD
            last_pos[x] = i
            
        return ans