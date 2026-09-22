class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        l=0
        cursum = 0
        for r in range(len(nums)):
            cursum += nums[r]
            # valid window
            while (cursum >= target):
                res = min(res, r-l+1)
                cursum -= nums[l]
                l+=1
        
            

        # cursum = sum(nums)


        # valid condition:
        # l,r = 0, len(nums) -1

        # while l <= r:
        #     res = min(res, r-l+1)
        #     # remove bigger element that keeps valid
        #     right = nums[r]
        #     left = nums[l]
        #     print(left, right)


        #     # dont evict if < target
        #     rightEvict = cursum - right >= target
        #     leftEvict = cursum - left >= target

        #     if leftEvict and rightEvict:
        #         # both can evict; remove max element
        #         if right > left: # r bigger
        #             cursum -= right
        #             r-=1
        #         else: # tie or left bigger
        #             cursum -= left
        #             l+=1
        #     else:
        #         if leftEvict:
        #             cursum -= left
        #             l+=1
        #         elif rightEvict:
        #             cursum -= right
        #             r-=1
        #         else:
        #             #neither so stop
        #             print("stop", nums[l:r+1])
        #             return res
                
        if res == len(nums) + 1:
            return 0
        return res

        # [2,1,5,1,5,3]
        # l.         r
        # target 10

        # l r   window.   res cursum
        # 0 5.  215153    6   17
        # 0 4.  21515.    5   14 evict 5 because itll make it under target
        # 1 4.  1515     4  12
        # 2 4   515.      3  11 STOP neither can pinch
        

         