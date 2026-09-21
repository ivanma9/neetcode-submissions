class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        # ans = [0] * len(temperatures)
        # for index, temp in enumerate(temperatures):

        #     while (stack) and temp > stack[-1][0]:
        #         top, i = stack.pop()
        #         ans[i] = (index-i)
        #     stack.append((temp,index))
        # return ans

        # monotonic stack
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                ind, t = stack.pop()
                res[ind] = i - ind
            stack.append((i, temperatures[i]))

        return res

