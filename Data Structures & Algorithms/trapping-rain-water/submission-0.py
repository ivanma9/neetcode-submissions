class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        water = 0

        left_bound = height[l]
        right_bound = height[r]

        while(l < r):
            # right bound is height >= leftbound
            if left_bound < right_bound:
                l+=1
                left_bound = max(left_bound, height[l])
                water += (left_bound - height[l])
            else:
                r-=1
                right_bound = max(right_bound, height[r])
                water += (right_bound - height[r])
        return water