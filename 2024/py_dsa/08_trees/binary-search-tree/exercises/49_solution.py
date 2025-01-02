class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if value is None:
            return False
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while temp:
            if new_node.value == temp.value:
                return False
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
        
                




##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################

print("\n----- Test: Insert to Empty Tree -----\n")
bst = BinarySearchTree()
assert bst.insert(5) is True
assert bst.root.value == 5
assert bst.root.left is None
assert bst.root.right is None

print("\n----- Test: Insert to Existing Tree -----\n")
bst = BinarySearchTree()
bst.insert(10)
assert bst.root.value == 10
assert bst.root.left is None
assert bst.root.right is None
bst.insert(5)
assert bst.root.left.value == 5
bst.insert(15)
assert bst.root.right.value == 15

print("\n----- Test: Insert Duplicate Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
assert bst.root.value == 10
bst.insert(5)
assert bst.root.left.value == 5
assert bst.insert(5) is False
assert bst.root.left.left is None
assert bst.root.left.right is None

print("\n----- Test: Insert Greater Than Root -----\n")
bst = BinarySearchTree()
bst.insert(10)
assert bst.root.value == 10
assert bst.insert(15) is True
assert bst.root.right.value == 15
assert bst.root.right.left is None
assert bst.root.right.right is None

print("\n----- Test: Insert Less Than Root -----\n")
bst = BinarySearchTree()
bst.insert(10)
assert bst.root.value == 10
assert bst.insert(5) is True
assert bst.root.left.value is 5
assert bst.root.left.left is None
assert bst.root.left.right is None


