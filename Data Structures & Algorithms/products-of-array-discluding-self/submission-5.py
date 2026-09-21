class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(1) space
        # at least len(nums) >= 2
        postfix = 1
        n = len(nums)
        res = [1] * n
        res[0] = nums[0]
        # res is prefix

        for i in range(1,n):
            res[i] = res[i-1] * nums[i]

        
        
        for i in range(n-1,0,-1):
            res[i] = res[i-1] * postfix
            postfix = nums[i] * postfix
        res[0]= postfix 
        return res

        # [1,2,4,6]

        # res = [1,2,12,8]
        # 1 , 2 , 8, 8
        # postfix = 1, 6, 24

        # actual = prefix[i-1] * suffix[i+1]
        # [48,48,24,6]
