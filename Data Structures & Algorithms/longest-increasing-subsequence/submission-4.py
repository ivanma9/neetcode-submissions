class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # over [i+1:]
        memo = {}
        def dfs(cur, i):
            if (cur,i) in memo:
                return memo[cur,i]
            if i == len(nums):
                return 1
            # skip if dec or same
            if cur >= nums[i]:
                return dfs(cur, i+1)

            # if increasing: use or skip
            ans = max(1 + dfs(nums[i], i+1),dfs(cur, i+1))
            memo[(cur,i)] = ans
            return ans
        LIS = 1
        for start in range(len(nums)):
            LIS = max(LIS, dfs(nums[start], start))
        
        return LIS
