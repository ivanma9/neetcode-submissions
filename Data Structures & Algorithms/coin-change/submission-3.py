class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if (amount == 0):
            return 0 

        # save every amount so that we can just add the 
        # types of coins when needing the "remainder"
        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if (i - coin >= 0):
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        print(dp)
        return dp[amount] if dp[amount] != float("inf") else -1           
