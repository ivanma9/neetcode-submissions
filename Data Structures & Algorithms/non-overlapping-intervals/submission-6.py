class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removed  =0
        prev_interval_start, prev_interval_end = intervals[0]
        for i in range(1, len(intervals)):
            st, ed = intervals[i]
            #check overlapping
            if prev_interval_end <= st:
                prev_interval_start = st
                prev_interval_end = ed
            # delete whichever has the larger ed
            else:
                if prev_interval_end > ed:
                    #remove end and update prev
                    prev_interval_start = st
                    prev_interval_end = ed

                removed+=1
        return removed
            # [1,2][1,4] -> 1,4
            # [1,5][1,4] -> 1,5
            # [1,4][2,3] -> 1,4
            # [1,4][2,5] -> 2,5

            # [1,4][5,6]
