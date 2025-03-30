from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        queue = deque()
        queue.append(self.root)
        while queue:
            temp = queue.popleft()
            if temp is None:
                self.root = new_node
                return

            # playing with the idea of raising assertions within the program
            assert (
                isinstance(temp, TreeNode) == True
            ), "temp is NOT an instance of TreeNode)"
            if temp.left is None:
                temp.left = new_node
                break
            elif temp.right is None:
                temp.right = new_node
                break
            else:
                queue.append(temp.left)
                queue.append(temp.right)
        return self.root

    def level_order_read(self, tree_values=list()):
        if not self.root:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            temp = queue.popleft()
            if temp:
                tree_values.append(temp.value)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return tree_values


new_tree = Tree()
min_heap_content = [14, 19, 16, 21, 26, 19, 68, 65, 30, 1000]
for num in min_heap_content:
    num, new_tree.insert(num)

assert new_tree.level_order_read() == [
    14,
    19,
    16,
    21,
    26,
    19,
    68,
    65,
    30,
    1000,
], "Error: MinHeap was not populated correctly!"


new_tree = Tree()
min_heap_content = []
for num in min_heap_content:
    num, new_tree.insert(num)

assert new_tree.level_order_read() == []
