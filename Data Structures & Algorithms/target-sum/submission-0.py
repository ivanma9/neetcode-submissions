class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (i, cur) -> total at this index so far
        def find_target(cur, i):
            # if (i >= len(nums)):

            if (i == len(nums) ):
                if (cur == target):
                    return 1
                else:
                    return 0
            if ((i,cur) in dp):
                return dp[(i,cur)]
            val = nums[i]
            dp[(i, cur)] = find_target(cur+val, i+1) + find_target(cur-val,i+1)
            return dp[(i,cur)]
        return find_target(0,0)    