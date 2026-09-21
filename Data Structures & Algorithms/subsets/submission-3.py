class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur_set,i):
            # base case
            if i == len(nums):
                res.append(cur_set.copy())
                return

            # recursive case
            
            # adding
            cur_set.append(nums[i])
            dfs(cur_set, i + 1)

            # not adding
            cur_set.pop()
            dfs(cur_set,i+1)

        dfs([], 0)
        return res

            