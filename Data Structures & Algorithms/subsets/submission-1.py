class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur, i):
            # base case
            print(cur, i)
            if i == len(nums):
                res.append(cur.copy())
                return
            # use cur for each index
            cur.append(nums[i])
            backtrack(cur, i + 1)
            cur.pop()
            backtrack(cur,i+1)
        backtrack([], 0)
        return res