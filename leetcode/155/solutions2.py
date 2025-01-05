"""
This solution solves this problem with O(1) time, O(n) space.
Hint: In this solution, we create a matrix, where each row contains two values
The top of the stack and the current minimum value.
"""


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            prv_min = self.stack[-1][1]
            new_min = min(val, prv_min)
            self.stack.append([val,new_min])

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()

    def top(self) -> None:
        if not self.stack:
            return
        top, min = self.stack[-1]
        return top

    def getMin(self):
        if not self.stack:
            return
        top, min = self.stack[-1]
        return min


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
