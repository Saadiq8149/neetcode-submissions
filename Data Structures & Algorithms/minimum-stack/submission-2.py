class MinStack:
    def __init__(self):
        self.stack = []
        self.prefixMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.prefixMin) == 0:
            self.prefixMin.append(val)
        else:
            self.prefixMin.append(min(val, self.prefixMin[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.prefixMin.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefixMin[-1]
        
