class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        # make prefix product
        # l ->r
        prefix = [nums[0]] * len(nums)
        postfix = [nums[len(nums)-1]] * len(nums)

        # 1 2 8 48
        for l in range(1,len(nums)):
            prefix[l] = prefix[l-1] * nums[l]
            r = len(nums) - l
            postfix[r-1] = postfix[r] * nums[r-1]
        print(prefix)
        print(postfix)
        # make postfix product
        # r to left
        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[1])
                continue
            if i == len(nums)-1:
                output.append(prefix[len(nums)-2])
                break #last
            prev = prefix[i-1]
            nt = postfix[i+1]
            output.append(prev * nt)
        return output
        





        