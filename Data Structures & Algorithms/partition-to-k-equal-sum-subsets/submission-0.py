class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        target = sum(nums)//k
        if sum(nums)%k != 0:
            return False
        used = [False]*n
        
        def backtrack(i,cursum, kk):
            if kk==0:
                return True
            if cursum == target:
                # add
                return backtrack(0,0,kk-1)
                
                
            
            for j in range(i, n):
                
                if used[j] or cursum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j+1,cursum+nums[j], kk):
                    return True
                used[j]= False
            return False

        return backtrack(0,0,k)


