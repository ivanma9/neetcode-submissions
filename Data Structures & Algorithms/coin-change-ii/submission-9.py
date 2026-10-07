class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo= {}
        def dfs(i,a):
            if (i,a) in memo:
                return memo[(i,a)]
            if i >= len(coins):
                return 0
            if coins[i] == a or amount ==0:
                return 1
            
            #rec
            #take
            res =0
            if a - coins[i] >= 0:
                res+= dfs(i, a-coins[i])
            #dont take
            res+=dfs(i+1, a)

            memo[(i,a)] = res
            return res
        return dfs(0,amount)