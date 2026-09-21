class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while (l <= r):
            mid = (l+r) // 2
            middle = nums[mid]
            if (middle == target):
                return mid
            print(middle)

            #find out if middle are on left side or right
            if (nums[l] <= middle):
                 #Left
                if (target < middle and nums[l] <= target ):
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                #middle on Right
                # 6 1 2 4 5 
                if (target > middle and target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

