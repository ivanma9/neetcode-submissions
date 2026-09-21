class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search looking decreasing interval
        # if normally sorted
        # numL < mid < numR
        # if rotated somehow
        # numL >= numR
        #     we need to find decreasing
        #     if r - l == 1:
        #         return r
        #     calc mid
        #     if mid <= R
        #         we should check [l:mid]
        #         8 2 3 4 5
        #     else mid > R
        #         we should check [mid: ]
        #         2 4 5 8  1
        #         45 [8 1] 2
        l = 0
        r = len(nums) - 1
        while (l < r and nums[l] >= nums[r]):
            if r- l == 1:
                return nums[r]
            mid = (r+l) // 2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid
        return nums[l]

        
