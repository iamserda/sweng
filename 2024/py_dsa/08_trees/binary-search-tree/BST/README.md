### 7. Binary Search Trees (BST)

#### README for Binary Search Trees

Binary Search Trees (BST) are a particular type of binary tree that facilitates efficient searching, insertion, and deletion operations. In a BST, for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater. This property allows for operations to proceed in a direction that halves the search space at each step, analogous to binary search in an array, providing efficient performance characteristics.

##### Key Operations

- **Search**: O(log n) on average, O(n) in the worst case (unbalanced tree)
- **Insertion**: O(log n) on average, O(n) in the worst case
- **Deletion**: O(log n) on average, O(n) in the worst case
- **Traversal**: In-order traversal of a BST will yield elements in sorted order.

##### Use Cases

- Implementing look-up tables that need to be frequently searched, inserted into, or deleted from.
- Managing sorted data for quick retrieval and manipulation.

##### Python Implementation

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

# Example usage
bst = BinarySearchTree()
bst.insert(3)
bst.insert(1)
bst.insert(4)
node = bst.search(1)
if node:
    print("Found:", node.value)  # Output: Found: 1
else:
    print("Not found")
```

#### Further Steps

- Implement delete functionality in the BST, considering cases where the node to be deleted has no children, one child, or two children.
- Explore self-balancing binary search trees like AVL trees and Red-Black trees to maintain efficient operation times even in the worst case.

Binary Search Trees provide a balanced approach to maintaining a collection of items that allows for efficient searching, insertion, and deletion operations. Heaps will be next!