class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] will store the max relative score difference starting from index i
        dp = [float('-inf')] * n + [0] 
        
        # Work backwards from the last stone
        for i in range(n - 1, -1, -1):
            take = 0
            # A player can take 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    take += stoneValue[i + k - 1]
                    # Maximize the score difference: (stones taken) - (opponent's best future score difference)
                    dp[i] = max(dp[i], take - dp[i + k])
        
        # dp[0] evaluates the game from the start (Alice's turn)
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"