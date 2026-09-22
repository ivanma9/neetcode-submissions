class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums) # O(n)
        prev = 0
        

        for color in range(3):
            ct = counts[color]
            for i in range(ct):
                nums[prev+i] = color
            prev = prev+ct
            print(color, ": ",nums)
        
            

        