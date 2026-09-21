class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        bank = [-1] * (amount + 1)
        bank[0] = 0
        
        for i in range(1, amount+1):
            for c in coins:
                # 1 coin
                if i -c == 0:
                    bank[i] = 1
                    # coin isnt too big and there exist a value seen using that coin
                elif i-c > 0 and bank[i-c] > 0:
                    if bank[i] == -1:
                        bank[i] = bank[i-c] + 1
                    else:
                        bank[i] = min(bank[i-c] + 1, bank[i])
                
        


        return bank[amount]