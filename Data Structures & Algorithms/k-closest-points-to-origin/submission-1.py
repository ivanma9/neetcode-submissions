class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        # (heap where max is at top)
        for x, y in points:
            dis = math.sqrt(x*x + (y*y))
            
            h.append([dis, x,y])
        
        heapq.heapify(h)
        print(h)

        res = []
        while(k>0):
            d,x,y = heapq.heappop(h)
            print(d)
            res.append([x,y])
            k-=1
        return res
