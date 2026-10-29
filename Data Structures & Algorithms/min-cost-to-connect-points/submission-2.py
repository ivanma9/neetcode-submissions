class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # dijkstra #V^2logv
        # track lowest cost dist
        # bfs, with a heap add smaller distances if found
        # connectivity
        # can go through each vertice O(n^2)
            # calc dist from each vertice
        #
        # start at first point
        graph = defaultdict(list)

        for x1,y1 in points:
            for x2,y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                d = abs(x1-x2) + abs(y1-y2)
                graph[(x1,y1)].append((d, (x2,y2)))

        heap = [(0,points[0])] # (0,[x,y])
        # dist = {k:float('inf') for k in graph.keys()}
        visited = set()
        N = len(graph)
        cost = 0
        while(heap):
            d, (x,y) = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            cost+=d
            if N == len(visited):
                return cost
            # track number of V visited to return
            for dd, (nx,ny) in graph[(x,y)]:
                # if what we hv now is better than exploring
                # continue
                if (nx,ny) in visited:
                    continue
                heapq.heappush(heap,(dd,(nx,ny)))

        return cost