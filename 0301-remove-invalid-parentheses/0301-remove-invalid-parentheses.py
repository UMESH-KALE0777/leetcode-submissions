class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Helper function to check if a string has valid parentheses
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        # Initialize the current level of our BFS with the original string
        level = {s}
        
        while True:
            # Filter the current level for only valid strings
            valid = list(filter(is_valid, level))
            
            # If we found valid strings, they are guaranteed to have the minimum removals
            if valid:
                return valid
            
            # If no valid strings were found, generate the next level by removing one parenthesis
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        # Slice out the character at index i
                        next_level.add(string[:i] + string[i+1:])
            
            # Move to the next level
            level = next_level