class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):

            while (stack) and temp > stack[-1][0]:
                top, i = stack.pop()
                ans[i] = (index-i)
            stack.append((temp,index))
        return ans