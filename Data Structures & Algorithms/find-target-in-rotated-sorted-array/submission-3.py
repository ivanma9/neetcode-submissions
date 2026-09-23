class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # target 1
        # left mid right
        # 3.   6.   2.    6 > 1
        # 1.   1    2.    1 == 1


        # target 6
        # 6123
        # l    m.   r
        # 6.   1.   3.    1 > 6 false 6 < 6
        # 6    6    6.  TRUE
        l,r = 0, len(nums)-1

        while (l<=r):
            m = (l+r) //2
            mid = nums[m]
            if mid == target:
                return m
            # if sorted left
            if nums[l] <= mid:
                if nums[l] <= target and target < mid:
                    r=m-1
                else:
                    l = m+1
            # sorted right
            elif mid <= nums[r]:
                if mid < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m -1

        return -1
            

            