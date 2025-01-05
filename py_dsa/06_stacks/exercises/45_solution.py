class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def sort_stack(stackA):
    if stackA.size() == 0:
        return
    stackB = Stack()  # to be loaded
    stackC = Stack()
    while stackA.size():
        stackB.push(stackA.pop())
    stackA.push(stackB.pop())
    count = 0
    while not stackB.is_empty() or not stackC.is_empty():
        count += 1
        print(f"BEFORE")
        print("B:", stackB.stack_list)
        print("C:", stackC.stack_list)
        print("A:", stackA.stack_list)
        stackA_value = stackA.pop()
        stackB_value = stackB.pop()
        if stackA_value >= stackB_value:
            stackA.push(stackA_value)
            stackC.push(stackB_value)
        else:
            stackA.push(stackB_value)
            stackC.push(stackA_value)

        if stackB.is_empty():
            if not stackC.is_empty():
                stackC, stackB = stackB, stackC
                stackA.push(stackB.pop())


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()


"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
