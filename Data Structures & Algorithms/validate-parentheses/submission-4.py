class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openP = {"(":")", "{":"}", "[":"]"}

        for l in s:
            if l in openP:
                stack.append(l)
            # close
            else:
                #match top of stack to l
                if stack:
                    if l != openP[stack.pop()]:
                        return False
                else:
                    # first is close
                    return False
        if len(stack) >0:
            return False
        return True

