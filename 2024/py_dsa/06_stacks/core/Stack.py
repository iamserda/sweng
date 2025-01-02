from Node import Node

class Stack:
    """Linked-List-based Stack"""
    def __init__(self, value=None):
        if value is None:
            self.top = None
            self.height = 0
        else:
            new_node = Node(value)
            self.top = new_node
            self.height = 1

    def insert(self, value):
        if value is None:
            return
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return self.top
    
    def pop(self):
        if not self.top:
            return
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
    def stack_to_arr(self):
        arr = []
        temp = self.top
        while temp is not None:
            arr.append(temp.value)
            temp = temp.next
        return arr

# Testing Arenas
new_stack = Stack()
new_stack.insert(10)
new_stack.insert(20)
new_stack.pop() # 20
new_stack.insert(30)
new_stack.insert(40)
new_stack.pop() # 40
new_stack.insert(50)
new_stack_arr = new_stack.stack_to_arr() # [50,30,10]
print(new_stack_arr, new_stack.height)