class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Step 1: Find the last occurrence index of each character
        last_occ = {char: i for i, char in enumerate(s)}
        
        stack = []
        visited = set()
        
        # Step 2: Iterate through the string
        for i, char in enumerate(s):
            # If the character is already in our result, skip it
            if char in visited:
                continue
            
            # Maintain monotonic increasing property where possible
            # Pop from stack if:
            # 1. The stack is not empty
            # 2. The current character is smaller than the top of the stack
            # 3. The top character appears again later in the string
            while stack and char < stack[-1] and last_occ[stack[-1]] > i:
                removed_char = stack.pop()
                visited.remove(removed_char)
                
            # Add the current character to both stack and visited set
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)