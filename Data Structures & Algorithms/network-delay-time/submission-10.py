class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph of times
        adjList = defaultdict(list)
        for u,v,t in times:
            adjList[u].append((v,t))

        # bfs
        # max (edges) is bottlneck
        # start at k
        # go through shortest and try to reach all
        heap = []
        minTime = float('inf')
        visited = set()
        heapq.heappush(heap, (0, k)) # min heap ascending

        while(heap):
            cur = heapq.heappop(heap)
            
            time, node = cur
            if node in visited:
                continue
            visited.add(node)

            if n == len(visited):
                return time
            for nei,t in adjList[node]:
                if nei in visited:
                    continue
                heapq.heappush(heap, (time + t, nei))
        
        return -1





