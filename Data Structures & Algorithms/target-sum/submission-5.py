class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def backtrack(i, cur):
            if i == n:
                if cur == target:
                    return 1  
                #out of bounds
                return 0
           
            # choose +
            return backtrack(i+1, nums[i] + cur) + backtrack(i+1, -nums[i] + cur)
        return backtrack(0, 0)


