class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(cur, visited):
            if len(cur) == n:
                res.append(cur.copy())
            for i in range(n):
                if nums[i] not in visited:
                    cur.append(nums[i])
                    visited.add(nums[i])
                    backtrack(cur, visited)
                    visited.remove(nums[i])
                    cur.pop()
        backtrack([], set())
        return res





