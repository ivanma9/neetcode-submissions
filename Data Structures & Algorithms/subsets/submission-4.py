class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur_set,i):
            # base case
            if i == len(nums):
                res.append(cur_set.copy())
                return

            # recursive case

            e = nums[i]
            
            # adding
            cur_set.append(e)
            dfs(cur_set, i + 1)

            # not adding
            cur_set.pop()
            while (i < len(nums) and nums[i] == e):
                i+=1
            dfs(cur_set,i)

        dfs([], 0)
        return res

            