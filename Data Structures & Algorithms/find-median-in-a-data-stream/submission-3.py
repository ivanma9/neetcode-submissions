class MedianFinder:

    def __init__(self):
        self.firstHalf = []
        # self.size = 0
        self.secondHalf = []


    def addNum(self, num: int) -> None:
        # self.size+=1
        m = len(self.firstHalf)
        n = len(self.secondHalf)
        # empty
        if self.firstHalf == [] and self.secondHalf == []:
            self.firstHalf.append(-num)
            return
        # only first has 1
        if self.secondHalf == []:
            t1 = -self.firstHalf.pop()
            min_element = min(num, t1)
            max_element = max(num, t1)
            self.firstHalf.append(-min_element)

            self.secondHalf.append(max_element)
            return       
        # if lengths are same and have smth in it:
        t1 = -self.firstHalf[0]
        t2 = self.secondHalf[0]

        if m == n:

            # case 3: t1 < t2 < num, 
            # t2 = heappop in h2,
            # heappush(h1, t2)
            # heappush(h2, num)
            if (t2 < num):
                t2 = heapq.heappop(self.secondHalf)
                heapq.heappush(self.firstHalf, -t2)
                heapq.heappush(self.secondHalf, num)
           
           
            # case 1: num <= t1 <= t2, heappush in h1

            # case 2: t1 <= num <= t2, heappush in h1
            else:
                heapq.heappush(self.firstHalf, -num)

        if m > n:
            # case 1: num <= t1 <= t2, 
            # t1 = heappop in h1,
            # heappush(h2, t1)
            # heappush(h1, num)
            if(num < t1):
                t1 = -heapq.heappop(self.firstHalf)
                heapq.heappush(self.secondHalf, t1)
                heapq.heappush(self.firstHalf, -num)
           

            # case 2: t1 <= num <= t2, 
            # heappush(t2, num)
    
            # case 3: t1 < t2 < num, 
            # heappush(t2,num)
            else:
                heapq.heappush(self.secondHalf, num)




    def findMedian(self) -> float:
        print(self.firstHalf)
        print(self.secondHalf)

        if len(self.firstHalf) == len(self.secondHalf):
            # avg of the tops of each half
            # even 
            return (-self.firstHalf[0] + self.secondHalf[0]) / 2
        # we store more elements if even in first

        return -self.firstHalf[0]

        