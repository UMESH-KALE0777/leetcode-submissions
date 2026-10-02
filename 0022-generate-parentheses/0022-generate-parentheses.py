class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Base case: if the string length is 2*n, it's a complete combination
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Rule 1: We can always add an open parenthesis if we haven't used all 'n' of them
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Rule 2: We can only add a close parenthesis if it has a matching open parenthesis
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return result