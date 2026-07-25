class Solution:
    def maxProduct(self, n: int) -> int:
        # Convert the number to a list of integer digits
        digits = [int(d) for d in str(n)]
        
        # Sort the digits in descending order
        digits.sort(reverse=True)
        
        # Return the product of the two largest digits
        return digits[0] * digits[1]