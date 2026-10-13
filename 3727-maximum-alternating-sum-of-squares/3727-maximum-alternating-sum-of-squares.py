class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # Step 1: Calculate the square of each number
        squares = [x * x for x in nums]
        
        # Step 2: Sort the squares in descending order
        squares.sort(reverse=True)
        
        # Step 3: Determine how many elements go to even (added) indices
        n = len(nums)
        num_added = (n + 1) // 2
        
        # Step 4: The largest squares are added, the remaining are subtracted
        return sum(squares[:num_added]) - sum(squares[num_added:])