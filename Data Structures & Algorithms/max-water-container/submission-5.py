class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max area
        # width gets smaller
        # keep best height
        # area is min(hei)x wdith
        # width = 0 is when l == r, imp

        l = 0
        r = len(heights) -1 
        area = 0
        while(l< r):
            width = r - l
            area = max(area, width * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return area
