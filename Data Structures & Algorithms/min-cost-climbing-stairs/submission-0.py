class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #recursive

        def climb(i):
            #base case
            # if current stair is past n we have reached top
            if i >= len(cost):
                return 0

            # pay cost of current square

            #recursive case
            # can choose i+1 or i+2
            

            return cost[i] + min(climb(i+1), climb(i+2))
        
        return min(climb(0), climb(1))