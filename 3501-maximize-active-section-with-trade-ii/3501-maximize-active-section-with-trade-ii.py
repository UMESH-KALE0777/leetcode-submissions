class Solution:
    def maxActiveSections(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        
        # Base count is the total '1's in the ENTIRE string `s`
        total_1s = s.count('1')
        
        # 1. Compress string into character segments
        seg_char = []
        seg_start = []
        seg_end = []
        seg_len = []
        seg_id = [0] * n
        
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            idx = len(seg_char)
            seg_char.append(s[i])
            seg_start.append(i)
            seg_end.append(j - 1)
            seg_len.append(j - i)
            for k in range(i, j):
                seg_id[k] = idx
            i = j
            
        m = len(seg_char)
        
        # 2. Precalculate max gain (val[j]) for fully interior '1' segments
        val = [0] * m
        for j in range(1, m - 1):
            if seg_char[j] == '1':
                val[j] = seg_len[j - 1] + seg_len[j + 1]
                
        # 3. Build Sparse Table for Range Maximum Query (RMQ)
        K = max(1, m.bit_length())
        st = [[0] * m for _ in range(K)]
        st[0] = val[:]
        
        for k in range(1, K):
            length = 1 << (k - 1)
            for i in range(m - (1 << k) + 1):
                st[k][i] = max(st[k - 1][i], st[k - 1][i + length])
                
        def query_rmq(L: int, R: int) -> int:
            if L > R:
                return 0
            k = (R - L + 1).bit_length() - 1
            return max(st[k][L], st[k][R - (1 << k) + 1])
            
        ans = []
        
        # 4. Process queries
        for l, r in queries:
            id_l, id_r = seg_id[l], seg_id[r]
            
            # If the entire range is within one segment, no trade is possible
            if id_l == id_r:
                ans.append(total_1s)
                continue
                
            # Find candidate boundary '1'-segments (must be STRICTLY inside bounds)
            j_min, j_max = -1, -1
            for j in range(id_l, min(id_r, id_l + 2) + 1):
                if seg_char[j] == '1' and seg_start[j] > l and seg_end[j] < r:
                    j_min = j
                    break
                    
            for j in range(id_r, max(id_l, id_r - 2) - 1, -1):
                if seg_char[j] == '1' and seg_start[j] > l and seg_end[j] < r:
                    j_max = j
                    break
                    
            # If there are no strictly internal '1'-segments, trade is impossible
            if j_min == -1:
                ans.append(total_1s)
                continue
                
            def calc_gain(j: int) -> int:
                left_len = min(seg_len[j - 1], seg_start[j] - l)
                right_len = min(seg_len[j + 1], r - seg_end[j])
                return left_len + right_len
                
            max_gain = max(calc_gain(j_min), calc_gain(j_max))
            
            # RMQ for '1'-segments whose surrounding '0's are fully intact inside [l, r]
            L_int, R_int = id_l + 2, id_r - 2
            if L_int <= R_int:
                max_gain = max(max_gain, query_rmq(L_int, R_int))
                
            ans.append(total_1s + max_gain)
            
        return ans

    # Alias to prevent AttributeError based on strict LeetCode test environment contexts
    def maxActiveSectionsAfterTrade(self, *args, **kwargs):
        return self.maxActiveSections(*args, **kwargs)