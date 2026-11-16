class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Continue rounds until the string length is <= k
        while len(s) > k:
            next_s = []
            
            # Step through the string in chunks of size k
            for i in range(0, len(s), k):
                chunk = s[i:i + k]
                # Calculate the sum of the digits in the current chunk
                chunk_sum = sum(int(digit) for digit in chunk)
                next_s.append(str(chunk_sum))
                
            # Merge the groups back together for the next round
            s = "".join(next_s)
            
        return s