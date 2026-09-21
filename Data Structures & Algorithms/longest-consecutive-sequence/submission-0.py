class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct = set(nums)
        maxS = 0
        for num in nums:
            # check whether num -1 is available
            temp = num
            #tryna find the beginning of streak

            streak = 1
            while temp-1 in distinct:
                streak +=1
                temp = temp-1
            # once temp-1 not available
            # this is beginning of streak
            while num + 1 in distinct:
                streak+=1
                num = num+1
            maxS = max(maxS, streak)
        return maxS