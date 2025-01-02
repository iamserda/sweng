
class MyStack:
    """Create a stack using two-queues"""
    def __init__(self):
        """stack constructor"""
        self.queue1 = []
        self.topmost = None
    def push(self, x: int) -> None:
        """add a new item to the top of the stack"""
        self.topmost = x
        self.queue1.append(self.topmost)

    def pop(self) -> int:
        """remove top-most item on the stack"""
        count = 0
        while count < len(self.queue1) - 1:
            self.topmost = self.queue1.pop(0)
            self.queue1.append(self.topmost)
            count += 1
        temp = self.queue1.pop(0)
        return temp
    
    def top(self) -> int:
        """return top"""
        return self.topmost if len(self.queue1) != 0 else None

    def empty(self) -> bool:
        """return true if the stack is empty, otherwise false."""
        return True if len(self.queue1) == 0 else False

# Testing Arenas:

# Test 1:
my_stack = MyStack()
my_stack.push(1)
my_stack.push(2)
print(my_stack.top() == 2)
my_stack.pop()
print(my_stack.top() == 1)
print(my_stack.empty())