class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_day_of_year(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_per_month[:month - 1]) + day
            
        arrive_A = to_day_of_year(arriveAlice)
        leave_A = to_day_of_year(leaveAlice)
        arrive_B = to_day_of_year(arriveBob)
        leave_B = to_day_of_year(leaveBob)
        
        overlap_start = max(arrive_A, arrive_B)
        overlap_end = min(leave_A, leave_B)
        
        return max(0, overlap_end - overlap_start + 1)