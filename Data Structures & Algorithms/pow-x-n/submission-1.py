class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n == 0):
            return 1
        if (n < 0):
            x = 1 /x
        
        ans = x
        for _ in range(abs(n)-1):
            ans *= x
        return ans