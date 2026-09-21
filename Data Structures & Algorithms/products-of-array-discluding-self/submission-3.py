class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix product
        # 1, 2, 8,24 #mult on left of number (prefix)
        # 48 48 24  6 1 # mult on right of number (postfix)
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        pre[0] = nums[0]
        post[-1] = nums[-1]
        # pre
        for i in range(1,len(nums)):
            pre[i] = pre[i-1]* nums[i]
            
        #post
        for i in range(len(nums)-2, -1,-1):
            post[i] = post[i+1]* nums[i]

        res =[1] * n

        res[0] = post[1]
        res[-1] = pre[-2]
        
        for i in range(1,len(nums)-1):
            res[i] = pre[i-1] * post[i+1]
        return res

        
