class Solution:
    def findMin(self, nums: List[int]) -> int:
        # goal is to find the pivot when e > e+1
        #sorted
        # until l==r

        l, r = 0, len(nums)-1
        while(l<r):
            mid = (l+r)//2
            print(mid)

            if nums[mid] > nums[r]:
                # check this and mid is not a candidate
                l = mid + 1
            else:
                # do not check this except include mid
                # nums mid <= nums r
                r = mid
        # l==r
        return nums[l]