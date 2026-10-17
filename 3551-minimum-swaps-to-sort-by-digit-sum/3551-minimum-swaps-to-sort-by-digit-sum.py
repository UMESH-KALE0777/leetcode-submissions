class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        n = len(nums)
        # Store (value, original_index)
        arr = [(nums[i], i) for i in range(n)]
        
        # Sort based on digit sum, then value
        arr.sort(key=lambda x: (get_digit_sum(x[0]), x[0]))
        
        visited = [False] * n
        total_swaps = 0
        
        for i in range(n):
            # If already visited or already in correct position
            if visited[i] or arr[i][1] == i:
                continue
            
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][1]
                cycle_size += 1
            
            if cycle_size > 0:
                total_swaps += (cycle_size - 1)
                
        return total_swaps