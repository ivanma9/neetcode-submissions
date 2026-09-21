class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for p in prices:
            if buy > p:
                buy = p
            else:
                sell = p - buy
                if profit < sell:
                    profit = sell
        return profit
