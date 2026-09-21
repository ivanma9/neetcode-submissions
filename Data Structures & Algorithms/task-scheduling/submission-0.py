class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()        

        # counts
        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)

        t = 0
    
        # go through maxHeap and queue
        while(maxHeap or queue):
            t +=1
            if maxHeap:
                l = heapq.heappop(maxHeap)
                # leftover
                # take curr time + wait
                l +=1
                if l != 0:
                    queue.append([l, (n + t)])
                
            # moving queue to maxheap
            if queue and queue[0][1] == t:
                heapq.heappush(maxHeap, queue.popleft()[0])
            
        return t


        