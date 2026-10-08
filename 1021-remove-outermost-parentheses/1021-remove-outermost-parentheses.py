class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0
        
        for char in s:
            if char == '(':
                # If balance is > 0, this is an inner parenthesis, so we keep it.
                if balance > 0:
                    result.append(char)
                balance += 1
            else:
                # Decrement balance first for closing parenthesis
                balance -= 1
                # If balance is still > 0, it's not the outermost closing parenthesis, keep it.
                if balance > 0:
                    result.append(char)
                    
        return "".join(result)