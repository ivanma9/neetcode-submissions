class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        profit = 0
        if len(prices) == 1:
            return 0
        for i in range(1, len(prices)):
            if prices[i] > buy:
                #can sell
                sell = prices[i]
                profit = max(profit, sell - buy)

            buy = min(prices[i], buy)
        return profit            