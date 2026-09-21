import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # try 1 to h is max num hours wih .t binary srearhc
        
        
        def eat_bananas(k):
            hours =0
            for pile in piles:
                hours += math.ceil(pile / k)
            if (hours <= h):
                return True
            return False
            
        
        l = 1
        r = max(piles)
        ans = r
        while (l<= r):
            
            mid = l + (r-l) //2
            print(l, r ,mid)
            if (eat_bananas(mid)):
                ans = min(mid, ans)
                r = mid - 1
            else:
                l = mid + 1

        return ans
            
        