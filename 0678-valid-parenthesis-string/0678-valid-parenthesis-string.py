class Solution:
    def checkValidString(self, s: str) -> bool:
        # min_open keeps track of the minimum possible open left brackets
        # max_open keeps track of the maximum possible open left brackets
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open = max(0, min_open - 1)
                max_open -= 1
            else: # char == '*'
                # '*' can be ')' (decreases min_open) 
                # '*' can be '(' (increases max_open)
                # '*' can be "" (does nothing to either boundary)
                min_open = max(0, min_open - 1)
                max_open += 1
            
            # If the maximum possible open brackets is less than 0, 
            # we have too many closing brackets at this point.
            if max_open < 0:
                return False
                
        # If min_open is 0, it means we can balance all left brackets.
        return min_open == 0