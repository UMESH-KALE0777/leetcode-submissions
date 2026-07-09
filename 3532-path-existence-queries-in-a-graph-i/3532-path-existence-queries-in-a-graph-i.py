class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # id_map[i] will store the component ID of node i
        id_map = [0] * n
        component_id = 0
        
        for i in range(1, n):
            # If the gap between adjacent elements is larger than maxDiff,
            # it starts a new connected component.
            if nums[i] - nums[i-1] > maxDiff:
                component_id += 1
            id_map[i] = component_id
            
        # For each query, u and v are connected if they share the same component ID
        ans = []
        for u, v in queries:
            ans.append(id_map[u] == id_map[v])
            
        return ans