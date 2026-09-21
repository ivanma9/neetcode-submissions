class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        2 heaviest stones, conditions
        - if x = y both pop
        - if x < y; x pop, y = y -x

        if no stones -> 0
        if stone -> return value

        option 1:
        sort stones, go from back to front, smashing with alg until 
        len(stack) <= 1

        option 2:
        [2,3,6,2,4]
        pq of len = 2
        [2, 3]
        [1]
        push elements to the heap
        [1, 6]
        [5]
        [5,2]
        [3,4]
        [1]
        if == then still do subtraction
        216
        6

        42
        2
        '''
        pq = [-s for s in stones]
        heapq.heapify(pq)
        
        while(len(pq) > 1):
            s1 = heapq.heappop(pq)
            s2 = heapq.heappop(pq)

            diff = -abs(s2 -s1)
            if diff != 0:
                heapq.heappush(pq, diff)
        return -pq[0] if len(pq) == 1 else 0

        
        
        



        
