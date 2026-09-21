class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy at the lowest sell at the highest difference after
        profit = 0
        buy = prices[0]
        for p in prices:
            sell = p
            buy = min(buy, p)
            
            if sell - buy >= profit:
                profit = sell - buy
            
        return profit