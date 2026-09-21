class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #go from 1 to amount
        coinset = set(coins)
        dp = [float('inf')] * (amount+1)
        if amount == 0: return 0
        for a in range(1, amount+1):
            #goal is fewest coins to get a
            # store in dp
            if a in coinset:
                dp[a] = 1
            else:
                for coin in coins:
                    if a - coin >= 0:
                        dp[a] = min(dp[a], 1 + dp[a-coin])
        return dp[amount] if dp[amount] != float('inf') else -1

