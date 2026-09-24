class MedianFinder:

    def __init__(self):
        self.firstHalf = [] # maxheap
        # want to be 1 more than second half or equal
        self.secondHalf = [] # min heap

    def addNum(self, num: int) -> None:


        # push to first 
        heapq.heappush(self.firstHalf, -num)
        #uneven
        if len(self.firstHalf) - len(self.secondHalf) >= 2:
            # old = pop off first
            old = -heapq.heappop(self.firstHalf)
            # push old to second
            heapq.heappush(self.secondHalf,old)
        # even or +/- 1
        else:
            # if wrong order
            if len(self.secondHalf) > 0 and -self.firstHalf[0] > self.secondHalf[0]:
                #adjust
                # old = pop off first
                old = -heapq.heappop(self.firstHalf)
                # push old to second
                heapq.heappush(self.secondHalf,old)
                
                old = heapq.heappop(self.secondHalf)
                # push old to second
                heapq.heappush(self.firstHalf,-old)
        

    def findMedian(self) -> float:
        if len(self.firstHalf) - len(self.secondHalf) == 1:
            return -self.firstHalf[0]
        else:
            return (-self.firstHalf[0] + self.secondHalf[0]) / 2
        
        