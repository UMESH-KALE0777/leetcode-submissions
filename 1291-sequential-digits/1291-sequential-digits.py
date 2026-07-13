class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        
        # Loop through all possible lengths of the sequential digits (from 2 to 9)
        for length in range(2, 10):
            # Slide a window of 'length' across the digits string
            for start in range(10 - length):
                num = int(digits[start:start + length])
                
                # If the number is within our target range, add it
                if low <= num <= high:
                    result.append(num)
                    
        return result