from collections import deque


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def recursive_insert(self, value):
        def recurse(_temp, _new):
            if _new.value > _temp.value:
                if not _temp.right:
                    _temp.right = _new
                    return True
                else:
                    return recurse(_temp.right, _new)
            elif _new.value < _temp.value:
                if not _temp.left:
                    _temp.left = _new
                    return True
                else:
                    return recurse(_temp.left, _new)
            return False

        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
            return True
        else:
            temp = self.root
            return recurse(temp, new_node)

    def insert(self, value) -> TreeNode:
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
        else:
            my_queue = deque()
            my_queue.append(self.root)
            while my_queue:
                temp = my_queue.popleft()
                if not temp.left:
                    temp.left = new_node
                    break
                elif not temp.right:
                    temp.right = new_node
                    break
                else:
                    my_queue.append(temp.left)
                    my_queue.append(temp.right)
        return self.root

    def print_binary_tree(self) -> None:
        "BFS traversal"
        arr = []

        arr.append(self.root)
        for index, elem in enumerate(arr):
            if elem.left:
                arr.append(elem.left)
            if elem.right:
                arr.append(elem.right)
            print(f"node #{index + 1}: {elem.value}")


# TESTING ARENAS:
#        8
#     /    \
#    10     1
#   /  \    /\
#  2   11  2  12

my_bin_tree = BinaryTree()
for i in [8, 10, 1, 2, 11, 2, 12]:
    my_bin_tree.insert(i)

my_bin_tree.print_binary_tree()
