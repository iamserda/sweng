from collections import deque

class Node:
    def __init__(self, value: any):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_recursive(self, value):

        def inserter(root, value):
            if not root:
                return Node(value)
            else:
                if value > root.value:
                    root.right = inserter(root.right, value)
                elif value < root.value:
                    root.left = inserter(root.left, value)
            return root

        self.root = inserter(self.root, value)
        return self.root

    def insert_iterative(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        temp = self.root
        while temp:
            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    break
                else:
                    temp = temp.right
                    continue
            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    break
                else:
                    temp = temp.left
                    continue
            else:
                break

    def remove(self, value):
        if not self.root:
            return

        def find_smallest_node(root) -> Node:
            temp = root
            while temp and temp.left:
                temp = temp.left
            return temp

        def rm(root, value) -> Node:
            if not root:
                return None
            if value > root.value:
                root.right = rm(root.right, value)
            elif value < root.value:
                root.left = rm(root.left, value)
            else:
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                else:
                    left_most = find_smallest_node(root.right)
                    root.value = left_most.value
                    root.right = rm(root.right, left_most.value)
            return root

        rm(self.root, value)
        return self.root

    def level_order_traversal(self):
        results = []
        _q = deque()
        _q.append(self.root)
        while _q:
            node = _q.popleft()
            if isinstance(node, Node):
                results.append(node.value)
                _q.append(node.left)
                _q.append(node.right)
        return results


my_bst = BinarySearchTree()
print("Pre:", my_bst.level_order_traversal())
for num in [8, 12, 4, 10, 14, 2, 6]:
    my_bst.insert_iterative(num)
print("Post addition:", my_bst.level_order_traversal())

print("Pre Removal:", my_bst.level_order_traversal())
for num in [8, 12, 4, 10, 14, 2, 6]:
    my_bst.remove(num)
    print(my_bst.level_order_traversal())
print("Pre Removal:", my_bst.level_order_traversal())
