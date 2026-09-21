class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # add all freq to heap (freq, val)
        heap = []
        hm = {}
        for n in nums:
            hm[n] = hm.get(n,0) + 1


        
        for kl,v in hm.items():
            heapq.heappush(heap,(-v , kl))
        
        ans = []
        for i in range(k):
            freq,o = heapq.heappop(heap)
            ans.append(o)
        return ans


        # pop off k elements as answer


        
