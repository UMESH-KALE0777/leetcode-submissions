class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        for i in range(n):
            distinct = set()
            for j in range(i, n):
                distinct.add(nums[j])
                count = len(distinct)
                total_sum += count * count
                
        return total_sum