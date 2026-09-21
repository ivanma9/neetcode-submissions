class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals
        # go through all the intervals
        # rather have earlier st time, and earlier end time
        # priortize earliest end time then earlier start time
        # [1,4][2,5]link use 1st
        # [1,4][2,3] 2nd inside
        # [2,3][2,4] link ise 1st
        # [1,3][1,4] use first
        # [1,4][1,3] use second 
        # [1,3][2,3]
        # [1,3][4,5]





        ct = 0
        intervals.sort()
        interval_st = intervals[0][0]
        interval_end = intervals[0][1]


        for i in range(1, len(intervals)):
            st,ed = intervals[i]
            # print("1",interval_st, interval_end)
            # print("2",st,ed)

            if interval_end <= st:
                #non overlap
                # update comparing interval (second interval)
                interval_st = st
                interval_end = ed 
            else:
                # overlapping
                if interval_end >= ed:
                    # use second if inside Full overlap or picking smaller interval
                    interval_st = st
                    interval_end = min(ed, interval_end)  
                ct+=1     
        return ct
