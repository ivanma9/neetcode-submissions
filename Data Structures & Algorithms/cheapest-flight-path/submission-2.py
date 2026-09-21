class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # idea: from src to dest
        # get all paths that are in k steps or less
        # minimize by taking cheapest total
        # lets do bfs
        # stop bfs if more than k steps
        paths = defaultdict(list)
        # st -> (price, ed)
        for st, ed, price in flights:
            paths[st].append((price, ed))
        
        q = [(src,0,0)]
        minCost = float('inf')
        while(q):
            curAirport, curCost,stops = q.pop(0)
            for path in paths[curAirport]:
                price, airport = path
                print(curAirport, airport, curCost, price, stops)
                #solution found
                if (stops > k):
                    continue
                if airport == dst:
                    minCost = min(minCost, curCost+price)
                if curCost+price < minCost:
                    q.append((airport, curCost+price, stops+1))
            
        return -1 if minCost == float('inf') else minCost

