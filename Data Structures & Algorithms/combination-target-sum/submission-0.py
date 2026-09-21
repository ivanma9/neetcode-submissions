class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # find every combination with the choice of any of nums
        res = []
        def backtrack(i, cur_sum, cur):
            if cur_sum == target:
                res.append(cur.copy())
                return
            for j in range(i,len(nums)):
                num = nums[j]
                if num + cur_sum <= target:
                    cur.append(num)
                    backtrack(j,num+cur_sum, cur)
                    cur.pop()
                
        backtrack(0,0, [])
        return res
