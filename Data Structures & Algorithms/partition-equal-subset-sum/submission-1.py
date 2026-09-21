class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        
        target = sum(nums) / 2
        if sum(nums) % 2 == 1:
            return False
        print(target)
        for i in range(len(nums)):
            nDP = set()
            for e in dp:
                if e + nums[i] == target:
                    return True
                nDP.add(e+ nums[i])
                nDP.add(e)
            dp = nDP
        return False

                
