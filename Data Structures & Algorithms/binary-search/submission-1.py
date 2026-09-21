class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while (l <= r):
            mid = (r + l) // 2
            if (nums[mid] == target):
                return mid
            if (nums[mid] < target):
                print("less", mid)
                l = mid +1
            elif (nums[mid] > target):
                print("more", mid)
                r = mid - 1
            print(l, r)
        return -1