class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #  1 2 0 1 0
        #  j j.  j j
        #  only can be considered possible if we reach the last index
        #  from index 0
        #  goal reach i = n-1 from i = 0

        #  brute force
        #  starting from i = 0 try nums[i] possibilities
        #  until reaching i = n-1
        #  this will O(n)
        #   (n-1) + n-2 + ...
        #   approx (n^2)
        #   and may never reach
    
        #  432100
        #  FFFFFT

        #  maybe lets go reverse?
        #  from each index can it reach the end?
        #  we will need to try every element in reverse
        #  o(n)
        #  i = 3 + e >= currecent = 6?
        #  update cur recent -> i
        #  4 1 0 3 0 01 0
        #             x j
        #  F F F T F F T T
        #        3-1 -11 0
        #          6 6 6 7
        #  still have to check the jumps
        n = len(nums)
        closest_jump = n-1
        for i in range(n-1, -1,-1):
            if (i + nums[i]) >= closest_jump:
                closest_jump = i
        return closest_jump == 0

         



