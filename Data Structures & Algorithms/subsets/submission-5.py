class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # choose or dont choose
        n = len(nums)
        res = []

        # backtrack (cur, i)
        def backtrack(cur,i):

            # base
            if i == n:
                res.append(cur.copy())
                return

            cur.append(nums[i]) 
            backtrack(cur,i+1) 
            cur.pop()
            backtrack(cur,i+1)

        backtrack([],0)
        return res