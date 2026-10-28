class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # target sum is current element find two elements on the right that add up to it.
        # proceed if we just did that target sum
        # if it reaches both branches triple + and -; crossed the 0 no solution with pivot i
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            # two pointer from i+1, n
            l = i+1
            r = len(nums)-1
            while l < r:
                
                triple = nums[l] + nums[r] + nums[i]
                # print(nums[i],"t", nums[l], nums[r], triple)
                if triple == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                if triple > 0:
                    r-=1
                if triple < 0:
                    l+=1

        return res