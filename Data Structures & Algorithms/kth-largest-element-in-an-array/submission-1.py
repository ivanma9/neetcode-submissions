class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #sort then return index k
        #O(k) + O (nlogn)

        # can we do it in o(n)?
        # use heap and save top k largest elements
        # heapq

        #O(nlog(k))
        heap = []
        
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i]) #O(logK)
            if (k < len(heap)):
                heapq.heappop(heap) # O(logk)
                
        return heap[0]



