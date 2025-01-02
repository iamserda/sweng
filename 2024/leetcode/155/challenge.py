class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_top = None
        self.minStack = []
        self.minStack_top = None

    def push(self, val: int) -> None:
        """Push: adds a element to the top of our stack"""
    def pop(self) -> None:
        """pop: removes the top element from the stack."""
    def top(self) -> int:
        """When possible, returns the value of the top-most element."""

    def getMin(self) -> int:
        """ In constant time... returns the min value of the stack"""

        
        
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