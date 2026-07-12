class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Get sorted unique elements
        sorted_unique = sorted(list(set(arr)))
        
        # Step 2: Create a mapping of element -> rank
        rank_map = {}
        for rank, val in enumerate(sorted_unique, 1):
            rank_map[val] = rank
            
        # Step 3: Transform the original array using the map
        return [rank_map[num] for num in arr]