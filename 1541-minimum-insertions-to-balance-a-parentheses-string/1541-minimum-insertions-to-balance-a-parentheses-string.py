class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_right = 0
        
        for char in s:
            if char == '(':

                if needed_right % 2 != 0:
                    insertions += 1
                    needed_right -= 1
                
                needed_right += 2
                
            else:  # char == ')'
                needed_right -= 1

                if needed_right < 0:
                    insertions += 1      # Insert the missing '('
                    needed_right += 2    # The new '(' requires two ')'. 
                                         # Since we just processed one, we still need one more.
                    
        return insertions + needed_right