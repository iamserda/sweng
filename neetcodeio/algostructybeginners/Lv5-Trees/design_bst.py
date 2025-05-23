class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f"key:{self.key}, val: {self.val}"


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key, val) -> None:
        """Given a key, and a val, creates a node:Node, and insert this node to the TreeMap."""
        if (key or val) is None:
            return
        new_node = Node(key, val)
        if not self.root:
            self.root = new_node
            return
        temp = self.root
        while temp:
            assert isinstance(temp, Node)
            if new_node.key == temp.key:
                temp.val = new_node.val
            elif new_node.key < temp.key:
                if temp.left:
                    temp = temp.left
                    continue
                else:
                    temp.left = new_node
            else:
                if temp.right:
                    temp = temp.right
                    continue
                else:
                    temp.right = new_node
            return

    @classmethod
    def search(cls, key: int, node) -> int:
        if not isinstance(node, Node):
            return -1
        if node.key == key:
            return node.val
        if key < node.key:
            return cls.search(key, node.left)
        if key > node.key:
            return cls.search(key, node.right)
        return -1

    def get(self, key: int) -> int:
        return TreeMap.search(key, self.root)

    def getMin(self) -> int:
        """return the value mapped to the SMALLEST key in the tree.
        If the tree is empty, return -1."""
        temp = self.root
        while temp and temp.left:
            temp = temp.left
        return temp.val

    def getMax(self) -> int:
        """Returns the value mapped to the largest key in the tree.
        If the tree is empty, return -1."""
        temp = self.root
        while temp and temp.right:
            temp = temp.right
        return temp.val

    def remove(self, key) -> None:
        """Removes the key-value pair with a given key located from the tree."""

        def rm(key, node):
            if node is None:
                return
            elif key > node.key:
                node.right = rm(key, node.right)
            elif key < node.key:
                node.left = rm(key, node.left)
            elif key == node.key:
                if not node.right and not node.left:
                    return
                elif not node.right:
                    return node.left
                elif not node.left:
                    return node.right
                else:
                    smallest_node = node.right
                    while smallest_node and smallest_node.left:
                        smallest_node = smallest_node.left
                    node.key = smallest_node.key
                    node.val = smallest_node.val
                    node.right = rm(smallest_node.key, node.right)
            return node

        self.root = rm(key, self.root)
        return self.root

    def dfs(root, arr):
        if not root:
            return
        TreeMap.dfs(root.left, arr)
        arr.append(root.key)
        TreeMap.dfs(root.right, arr)

    def getInorderKeys(self) -> list[int]:
        """Returns an list of the keys in the tree in ascending order."""

        arr: list[int] = []
        TreeMap.dfs(self.root, arr)
        return arr


# Test-Driven Development
new_tmap = TreeMap()
new_tmap.insert("Ronaldo", 1976)
new_tmap.insert("Jordan", 1963)
new_tmap.insert("Bryant", 1978)
new_tmap.insert("Messi", 1987)
assert new_tmap.getInorderKeys() == ["Bryant", "Jordan", "Messi", "Ronaldo"]
assert new_tmap.get("Ronaldo") == 1976
assert new_tmap.get("Messi") == 1987
assert new_tmap.get("Jordan") == 1963
# Kobe's Year of birth, because (B) in key 'Bryant' is first when ordered from left-to-right
assert new_tmap.getMin() == 1978
# Kobe's Year of birth, because (R) in key 'Ronaldo' is first when ordered from left-to-right
assert new_tmap.getMax() == 1976
new_tmap.remove("Bryant")
assert new_tmap.getInorderKeys() == ["Jordan", "Messi", "Ronaldo"]
new_tmap.remove("Jordan")
assert new_tmap.getInorderKeys() == ["Messi", "Ronaldo"]
new_tmap.remove("Messi")
assert new_tmap.getInorderKeys() == ["Ronaldo"]
new_tmap.remove("Ronaldo")
assert new_tmap.getInorderKeys() == []

# TEST SUITE 2 from Neetcode:
new_tmap.insert(1, 2)
new_tmap.insert(4, 2)
new_tmap.insert(3, 7)
new_tmap.insert(2, 1)
assert new_tmap.getInorderKeys() == [1, 2, 3, 4]
new_tmap.remove(1)
assert new_tmap.getInorderKeys() == [2, 3, 4]
