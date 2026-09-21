class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for i, num in enumerate(nums):
            # if num in hm and num == target-num and i == hm[num]:
            #     continue
            if target - num in hm:
                return [hm[target-num], i]
            hm[num] = i 

        