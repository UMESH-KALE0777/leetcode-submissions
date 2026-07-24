class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # Step 1: Remove duplicates as they don't contribute to new unique XOR combinations
        unique_nums = set(nums)
        
        # Step 2: Start with 0. 
        # We will apply XOR 3 times to simulate picking 3 elements.
        current_xors = {0}
        
        # Step 3: Expand the set 3 times
        for _ in range(3):
            # Use a set comprehension for fast C-level execution in Python
            current_xors = {x ^ y for x in current_xors for y in unique_nums}
            
        # Step 4: The size of the set is our number of unique XOR triplets
        return len(current_xors)