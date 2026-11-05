class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        dist = [float('inf') for i in range(n+1)]
        heap = [(0,k)]
        visited = set()
        # ct = 0
        while(heap):
            w, cur = heapq.heappop(heap)
            if w > dist[cur]:
                continue
            # ct +=1
            visited.add(cur)
            if len(visited) == n:
                return w
            
            
            for nei, nw in graph[cur]:
                if w+ nw >= dist[nei]:
                    continue
                heapq.heappush(heap,(w+nw, nei))
                dist[nei] = w+nw
            
        return -1






