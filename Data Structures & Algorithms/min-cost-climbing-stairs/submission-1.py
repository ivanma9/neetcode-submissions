class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #recursive

        # def climb(i):
        #     #base case
        #     # if current stair is past n we have reached top
        #     if i >= len(cost):
        #         return 0
        #     # pay cost of current square

        #     # can choose i+1 or i+2
        #     return cost[i] + min(climb(i+1), climb(i+2))
        
        # return min(climb(0), climb(1))
        n = len(cost)
        dp = [0] * (n+1)
        if n == 2:
            return min(cost[0], cost[1])
        for i in range(2,n+1):
            dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
            print(dp)
        return dp[n]