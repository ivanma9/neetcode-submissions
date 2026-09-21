class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        finalIntervals = []
        tempInterval = intervals[0]
        for i in range(1, len(intervals)):
            curInterval = intervals[i]

            if tempInterval[1] >= curInterval[0]:

                tempInterval[1] = max(tempInterval[1],curInterval[1])
            else:
                finalIntervals.append(tempInterval)
                tempInterval = curInterval
        finalIntervals.append(tempInterval)
        return finalIntervals                                                                                                                             