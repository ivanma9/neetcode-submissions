class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #    position = [10,8,0,5,3], speed = [2,4,1,1,3]
    #    times = [1,1,7,3, 12]
    #    t = 1     2. 3 
    #    10: 11 : 12 
    #    8:  12 merge to car 10
    #    0.  1.   2.  3. 4. 5 6 7 8 9 10 11 12
    #    5:  6.   7. 8.  9 10 1112
    #    3. 6.   merge with car 5

    #    t = p/s

        times = [(position[i], (target-position[i])/speed[i]) for i in range(len(position))]
        times.sort(reverse=True)
        stack = []
        for pos, t in times:
            if stack and t <= stack[-1][1]:
                # merge join fleet:
                continue

            else:
                # new fleet
                stack.append((pos,t))
        return len(stack)
