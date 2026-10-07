class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # distinct combos 
        dp = [0]*(amount+1)
        dp[0] = 1

        # 2367 9
        # 2:2
        # 3:3
        # 4:22
        # 5:23 not 32
        # 6:6 222 33 not 222
        # 7:
        for coin in coins[::-1]:
            # find combinations
            for cur_amount in range(1,amount+1):
                if cur_amount - coin >=0:
                    dp[cur_amount] = dp[cur_amount-coin] + dp[cur_amount]
                else:
                    dp[cur_amount] = dp[cur_amount]
        return dp[amount]