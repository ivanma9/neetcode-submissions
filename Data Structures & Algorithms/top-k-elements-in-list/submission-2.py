class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = []
        for kk,v in count.items():

            if len(heap) == k:
                print("hi")
                min_elem = heapq.heappop(heap)
                if (min_elem[0] < v):
                    heapq.heappush(heap, (v,kk))
                else:
                    heapq.heappush(heap, min_elem)
            else:
                heapq.heappush(heap, (v,kk))
        return [kk for v,kk in heap]
