class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack and val < self.min_stack[-1]:
            popped = self.min_stack.pop()
            self.min_stack.append(val)
            self.min_stack.append(popped)
        else:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
        self.min_stack.pop() if popped == self.min_stack[-1] else None
    
    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()