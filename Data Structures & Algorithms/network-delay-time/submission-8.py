class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        visit = set()
        # map node : [(children, cost)]
        network = defaultdict(list)
        for s, e, t in times:
            network[s].append((e,t))

        # starting from k, bfs through the nodes 
        # track the visited
        # could add to bfs (node, cost)
        # every time a node is traversed reduce cost
        # hwoever, bad because we dont wanna update the
        # whole array after every traversal.
        # A BETTER WAY
        # save the min time to reach each node
        # do greedy dfs
        # go the way that is smaller cost
        # increment time by cost

        minHeap = [(0,k)] # first value is heap sorted based (Weight)
        while (minHeap):
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time = cost

            for child, w2 in network[node]:
                if child not in visit:
                    heapq.heappush(minHeap, (cost + w2, child))

            # for child, w2 in network[node]:
            #     if child not in visit:
            #         heapq.heappush(minHeap, (cost + w2, node))
        

        # diff " routes" are based on indegree edges
        # add next node 
        # also add to set so we know there is a decision to be made, but it is 
        # in the bottom of the stack 
        # accumulate cost
        # when adding to stack, take (node,cost + time)
        
        # when reaching the node if not in visit-> 
        # add to visit
        # and inc cost because this is first time seeing node
        # if node alr visited 
        # compare visit node pair to new cost
        # take min


        return time if len(visit) == n else -1