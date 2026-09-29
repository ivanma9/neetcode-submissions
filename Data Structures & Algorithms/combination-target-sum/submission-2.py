class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 9 - cand = 7
        # []
        res = []
        def backtrack(cur,t, i ):
            if t == 0:
                res.append(cur.copy())
                return
            for j in range(i, (len(nums))):
                cand = nums[j]
                if t - cand >= 0:
                    cur.append(cand)
                    backtrack(cur, t-cand, j)
                    cur.pop()
        backtrack([],target,0)
        return res
            