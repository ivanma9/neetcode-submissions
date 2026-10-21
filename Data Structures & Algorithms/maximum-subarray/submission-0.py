class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = maxsum
        for i in range(1,len(nums)):
            cursum = max(nums[i], cursum+nums[i])
            maxsum = max(cursum, maxsum)
        return maxsum