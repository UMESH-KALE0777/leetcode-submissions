class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        # If the required sum exceeds the maximum possible sum with 'num' digits
        if sum_val > 9 * num:
            return ""
        
        # Calculate the count of 9s and the remainder digit
        num_9 = sum_val // 9
        rem = sum_val % 9
        
        # Calculate the remaining number of 0s needed
        num_0 = num - num_9 - (1 if rem > 0 else 0)
        
        # Build the largest lexicographical string
        ans = ["9"] * num_9
        if rem > 0:
            ans.append(str(rem))
        ans.append("0" * num_0)
        
        return "".join(ans)