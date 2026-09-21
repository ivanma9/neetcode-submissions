class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        ans= []
        
        for kk,v in hm.items():

            heapq.heappush(ans, (-v, kk))
        res = []
        while (k >0):
            res.append(heapq.heappop(ans)[1])
            k-=1
        return res        
