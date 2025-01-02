# This solution's pop is still technically O(n)
# It needs to find a new minimum if the last minimum was popped.

class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_top = None
        self.minStack = []
        self.minStack_top = None

    def push(self, val: int) -> None:
        self.stack_top = val
        self.stack.append(self.stack_top)
        if not self.minStack:
            self.minStack.append(self.stack_top)
        else:
            self.minStack.append(min(self.minStack.pop(), self.stack_top))

    def pop(self) -> None:
        popped = self.stack.pop()
        if not self.stack:
            self.minStack_top = self.stack_top = None
            self.minStack = []
            return
        self.stack_top = self.stack[-1]
        if popped == self.getMin():
            self.minStack = [float("inf")]
            for item in self.stack:
                self.minStack.append(min(self.minStack.pop(), item))

    def top(self) -> int:
        return self.stack_top

    def getMin(self) -> int:
        return self.minStack[0] if self.minStack else None


# TESTING ARENAS:

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

