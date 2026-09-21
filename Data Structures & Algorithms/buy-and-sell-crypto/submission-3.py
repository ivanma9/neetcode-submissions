class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # finding the max difference
        '''
        A1
        between 2 stocks 
        I would rather choose the smaller stock to buy
        unless last index

        if last index (eith sell now or shouldve sold before)
        
        approach one save minimum up to index i
        and max up to max from n-1 backwards

        10 1 1 1 1 1
        10 7 7 7 7 1

        max - min


        n = len(prices)
        maxs = [prices[n-1]] * n
        mins = [prices[0]] * n
        profit = 0
        for i in range(1,n):
            mins[i] = min(mins[i-1], prices[i])
        for i in range(n-2,-1,-1):
            maxs[i] = max(maxs[i+1], prices[i])
        for i in range(n):
            profit = max(profit, maxs[i] -mins[i])
        return profit
        '''
        
        # A2
        # from 0 -> n
        if len(prices) == 1:
            return 0
        buy_stock = prices[0]
        profit = 0
        for i in range(len(prices)):
            cur_stock = prices[i]

        # if cur stock is less than buy stock than
        #     update buy stock = cur stock
            if cur_stock < buy_stock:
                buy_stock = cur_stock
            else:
            #     this should not get changed unless we see a 
            #     smaller stock to buy
                profit = max(profit, cur_stock - buy_stock)
        #     possbility to sell or hold
        #     profit = max(cur - buy)
        return profit


