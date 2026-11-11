class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Candidate 1: Buy exactly 0 bundle items
        ans1 = (need1 * cost1) + (need2 * cost2)
        
        # Candidate 2: Buy exactly enough bundle items to fulfill the smaller need
        min_need = min(need1, need2)
        ans2 = (min_need * costBoth) + ((need1 - min_need) * cost1) + ((need2 - min_need) * cost2)
        
        # Candidate 3: Buy exactly enough bundle items to fulfill the maximum need
        max_need = max(need1, need2)
        ans3 = max_need * costBoth
        
        # The optimal cost will mathematically always be one of these three options
        return min(ans1, ans2, ans3)