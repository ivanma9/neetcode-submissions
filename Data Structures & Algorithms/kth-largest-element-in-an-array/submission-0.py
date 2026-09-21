class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #sort then return index k
        #O(k) + O (nlogn)

        # can we do it in o(n)?
        # use heap and save top k largest elements
        # heapq

        #O(nlog(k))
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        
        
        for i in range(k, len(nums)):
            if (nums[i] > heap[0]):
                heapq.heappop(heap) # O(1)
                heapq.heappush(heap, nums[i]) #O(logK)
        return heap[0]



