class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) -1

        maxarea = 0

        while(l<r):

            width = r - l

            height = min(heights[l], heights[r])

            area = height * width
            maxarea= max(area,maxarea)

            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return maxarea