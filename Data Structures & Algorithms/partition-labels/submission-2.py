class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # find first and last insce of each char
        #create intervals for each letter
        # see overlapping intervals as 1 string of size min,max

        hm = {}
        hm2 = {}


        #lr

        for i in range(len(s)):
            l  = s[i]
            if l not in hm:
                hm[l]= i
        #rl
        for i in range(len(s)-1,-1,-1):
            l  = s[i] 
            if l not in hm2:
                hm2[l]= i
        
        intervals = []
        for k in hm.keys():
            intervals.append((hm[k], hm2[k], k))
        # should be sorted
        #merge overlapping
        curStart = intervals[0][0]
        curEnd = intervals[0][1]
        res = []
        for i in range(1,len(intervals)):
            st,ed,k = intervals[i]
            if curEnd > st:
                #merge
                curStart = min(curStart, st)
                curEnd = max(curEnd, ed)
            else:
                #append cur , nonoverlapping

                res.append(curEnd - curStart + 1)
                curStart = st
                curEnd = ed


        res.append(curEnd - curStart + 1)
        return res





