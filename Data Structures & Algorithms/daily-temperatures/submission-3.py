class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = [1,4,1,2,1,0,0]
        # stack 40,5 28,6 
        # subtract indices
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                tt,ii = stack.pop()

                res[ii] = i - ii
            stack.append((t,i))

        return res
                
                
        
        

