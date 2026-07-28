class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        
       
        counts = Counter(s)
        
        first_half = []
        middle = ""
        
     
        for char in "abcdefghijklmnopqrstuvwxyz":
            if counts[char] > 0:
               
                first_half.append(char * (counts[char] // 2))
                
                
                if counts[char] % 2 != 0:
                    middle = char
                    
     
        half_str = "".join(first_half)
        
      
        return half_str + middle + half_str[::-1]