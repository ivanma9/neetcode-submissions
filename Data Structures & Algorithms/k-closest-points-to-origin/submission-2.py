class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = [] # (dist, [x,y])
        # heapq.heapify(pq)
        for x,y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(pq, [-dist, x,y])
            print("Before", pq)
            if len(pq) > k:
                heapq.heappop(pq)
            print(pq)
        ans = []
        while (len(pq) > 0):
            dist,x,y = heapq.heappop(pq)
            ans.append([x,y])

        return ans
                
