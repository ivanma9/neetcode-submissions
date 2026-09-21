class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # -4 -1 -1 0 1 2

        # -4 -1 2 -3
        # -4 -1 2 -3
        # -4 0 2 -2
        # -4 1 2  -1 -4 2 2 stop dup
        # -1 -1 2 0


        n = len(nums)
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n -1
            while (l < r):
                s =nums[i] + nums[l] + nums[r]
                if s > 0:
                    r-=1
                elif s < 0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res


