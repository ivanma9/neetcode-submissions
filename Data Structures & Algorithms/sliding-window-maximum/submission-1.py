class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res =[]
        heap = []# size k,  max heap on top

        
        for r in range(n):
            # res.append(max(nums[l:l+k]))
            heapq.heappush(heap,(-nums[r],r))
            if r >= k-1:
                while (heap[0][1] <= r-k):
                    heapq.heappop(heap)
            
                res.append(-heap[0][0])
        
        return res
            