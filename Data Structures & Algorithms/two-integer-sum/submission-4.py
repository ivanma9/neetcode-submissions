class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}

        for i, n in enumerate(nums):
            if (target-n) in counts:
                return [counts[target-n] ,i]
            counts[n] = i

        return [-1,-1]