class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # add all freq to heap (freq, val)
        heap = []
        hm = {}
        for n in nums:
            hm[n] = hm.get(n,0) + 1


        
        for kl,v in hm.items():
            heapq.heappush(heap,(v , kl))
            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)

        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans




        
