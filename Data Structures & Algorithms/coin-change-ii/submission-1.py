class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 1 2 3 target 4
        # O(coins ^ amount) backtrack
        # save repeated
        
        dp = [[0] * (amount + 1) for i in range(len(coins) +1)]
        for i in range(len(coins) +1):
            dp[i][0] = 1
        
        for cur_amount in range(1,amount+1):
            for i in range(len(coins)):
                coin = coins[i]

                dp[i+1][cur_amount] += dp[i][cur_amount]
        
                diff = cur_amount - coin

                if diff >= 0:
                    dp[i+1][cur_amount] += dp[i+1][diff]
 
            
        return dp[len(coins)][amount]
# 7 - coin =2 = 5
            
        # for each coin we can take or not take
        # if we choose to take we can choose any coin
        # to up to where i is including itself
        # to avoid duplicates like 1112 and 2111
        # we do this for every decision

        # optomize later
        # lets keep a dp and say for every count we reach
        # 111 for 3 and add it 1 possibility for 3
        # when we can take dp[3]


        # 0 0
        # 1 0
        # 2 1 2
        # 3 0
        # 4 2 22 4
        # 5 0
        # 6 2 222 24
        # 7 0


#         1 = 1 1 
#         2 = [2, 11] 2
#         3 = [3, 12, 111] 3
#         4 = [13, 112, 1111, 22] 4
#         3 - 4
#         5 = [113,1112, 11111, 122, 23] 5
#         6 + 4 = 10 - 5 = 5
#         6 = [1113,11112, 111111, 1122, 123, 
#         222, 33,] 7
#         5 + 8 
#         13 - 6 = 7
#         dp[1] + dp[3]

#         dp [2] + dp[2]
#         [1][]
#     [11]
# [111][1111][11111]

#     dp1 + dp4
#     dp2 + dp3