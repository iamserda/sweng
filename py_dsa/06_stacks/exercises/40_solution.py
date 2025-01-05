# Exercises 40(constructor), 41(push, pop), 42(peek, getSize)

class Stack:
    def __init__(self):
        self.stack_list = []
        self.height = len(self.stack)
    
    def push(self, value):
        self.stack_list.append(value)
    
    def peek(self):
        return None if self.getSize() <= 0 else self.stack_list[-1]
    
    def getSize(self):
        return len(self.stack_list)
    
    def pop(self):
        return self.stack_list.pop() if self.size() > 0 else None
    