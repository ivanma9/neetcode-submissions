class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        prev = nums[0]
        best = max(nums[0],nums[1])
        if len(nums) == 2:
            return best
        n =len(nums)
        for i in range(2,n-1):
            temp = best
            best = max(best, prev+nums[i])
            prev = temp
        firstBest = best
        
        prev = nums[-1]
        best = max(nums[0],prev)
        for i in range(1,n-2):
            temp = best
            best = max(best, prev+nums[i])
            prev = temp

        return max(firstBest, best)
        
        