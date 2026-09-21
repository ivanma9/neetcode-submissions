class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        # sort intervals by endi
        intervals.sort(key=lambda x : x[1])
        print(intervals)
        # comparing i,j
        # if j_st smaller than i_ed than remove jth
        # inc count
        # increase j+=1
        # else
        # need to increase i= j and j += 1
        # return count
        count = 0
        i = 0
        j = 1
        while (j < len(intervals)):
            print(i,j)
            if (intervals[j][0] < intervals[i][1]):
                count +=1
            else:
                i = j

            j += 1
        return count