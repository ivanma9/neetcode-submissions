class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [0 for _ in range(n)]
        if n == 1:
            return nums[0]
        prev =nums[0]
        best = max(nums[0], nums[1])
    
   
        for i in range(2,n):
            # if best < prev + nums[i]:
                #use nums[i] and prev
                # prev = best+ nums[i]
            prev, best = best, max(prev + nums[i], best)
        return best