class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        balance = 0
        
        for char in s:
            if char == '(':
                balance += 1
            else:  # char == ')'
                if balance > 0:
                    balance -= 1
                else:
                    open_needed += 1
                    
        # Total moves = missing '(' + unmatched '(' that need ')'
        return open_needed + balance