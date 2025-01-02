"""
This solution solves this problem with O(1) time, O(n) space.
Hint: We save(and remove) all newly found(popped) min values.
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_top = None
        self.minStack = []
        
    def push(self, val)->None:
        self.stack_top = val
        self.stack.append(self.stack_top)
        if not self.minStack:
            self.minStack.append(self.stack_top)
        elif self.stack_top <= self.minStack[-1]:
            self.minStack.append(self.stack_top)
    
    def pop(self)->None:
        popped = self.stack.pop()
        if popped == self.minStack[-1]:
            self.minStack.pop()
        
        if self.stack:
            self.stack_top = self.stack[-1]
        else:
            self.stack_top = None
            self.minStack = []
    
    def top(self):
        return self.stack_top
    
    def getMin(self)->int:
        if self.stack:
            return self.minStack[-1]
        
my_stack = MinStack()
my_stack.push(0)
my_stack.push(10)
my_stack.push(-10)
assert my_stack.getMin() == -10
assert my_stack.top() == -10
my_stack.pop()
assert my_stack.getMin() == 0
assert my_stack.top() == 10
my_stack.pop()
my_stack.pop()
assert my_stack.getMin() == None
assert my_stack.getMin() == None