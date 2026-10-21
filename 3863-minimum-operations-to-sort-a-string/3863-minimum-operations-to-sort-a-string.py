class Solution:
    def minOperations(self, s: str) -> int:
        sorted_s = "".join(sorted(s))
        
        if s == sorted_s:
            return 0
            
        n = len(s)
        
        # Find the boundaries of the mismatched segment
        L = 0
        while L < n and s[L] == sorted_s[L]:
            L += 1
            
        R = n - 1
        while R >= 0 and s[R] == sorted_s[R]:
            R -= 1
            
        # If the mismatched segment is smaller than the whole string, 1 operation is enough
        if R - L + 1 < n:
            return 1
            
        # If n <= 2 and it's out of order, proper substrings are length 1, so it's impossible
        if n <= 2:
            return -1
            
        min_char = min(s)
        max_char = max(s)
        
        # Worst-case scenario: unique max at the start AND unique min at the end
        if s[0] == max_char and s.count(max_char) == 1 and \
           s[-1] == min_char and s.count(min_char) == 1:
            return 3
            
        # For all other cases, 2 operations are sufficient
        return 2