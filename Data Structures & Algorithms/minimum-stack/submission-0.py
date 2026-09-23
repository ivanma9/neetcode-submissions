class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minVal:
            self.minVal.append(min(self.minVal[-1], val))
        else:
            self.minVal.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minVal.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal[-1]
        
