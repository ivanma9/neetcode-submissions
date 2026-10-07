class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(rate):
            total_hours = 0
            for bananas in piles:
                total_hours += math.ceil(bananas / rate)
            if total_hours > h:
                return False
            return True
        l = 1
        r = max(piles)
        # return mid which will be l==r
        while(l<r):
            mid = (l+r) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1

        return l


        