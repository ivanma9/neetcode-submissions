class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n ==2:
            return 2
        prev = 1
        prev2 = 2
        for i in range(3,n+1):
            temp = prev
            prev = prev2
            prev2 = temp + prev2

        return prev2