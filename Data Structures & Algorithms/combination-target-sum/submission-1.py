class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        numset = set(nums)
        res = []

        def backtrack(i, cur_sum, cur):
            if i >= len(nums) or cur_sum > target:
                return
            if cur_sum == target:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            backtrack(i, cur_sum + nums[i], cur)
            cur.pop()
            backtrack(i+1, cur_sum, cur)
        backtrack(0, 0, [])
        return res