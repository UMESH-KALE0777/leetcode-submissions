import bisect
from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        n2 = len(arr2)
        
        for x in arr1:
            idx = bisect.bisect_left(arr2, x)
            
            # Check element at idx (if exists)
            has_close_element = False
            if idx < n2 and abs(arr2[idx] - x) <= d:
                has_close_element = True
                
            # Check element at idx - 1 (if exists)
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                has_close_element = True
                
            if not has_close_element:
                count += 1
                
        return count