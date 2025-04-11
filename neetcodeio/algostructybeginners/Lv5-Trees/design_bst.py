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
        if not key or not val:
            return
        new_node = Node(key, val)
        if not self.root:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                if new_node.key < temp.key:
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
                break

    def get(self, key: int) -> int:
        pass

    def getMin(self) -> int:
        """return the value mapped to the SMALLEST key in the tree.
        If the tree is empty, return -1."""
        pass

    def getMax(self) -> int:
        """Returns the value mapped to the largest key in the tree.
        If the tree is empty, return -1."""
        pass

    def remove(self, key) -> None:
        """Removes the key-value pair with a given key located from the tree."""
        pass

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
# assert new_tmap.get("Ronaldo") == 1976
# assert new_tmap.get("Messi") == 1987
# assert new_tmap.get("Jordan") == 1963
# # Kobe's Year of birth, because (B) in key 'Bryant' is first when ordered from left-to-right
# assert new_tmap.getMin() == 1978
# # Kobe's Year of birth, because (R) in key 'Ronaldo' is first when ordered from left-to-right
# assert new_tmap.getMax() == 1976
# new_tmap.remove("Bryant")
# assert new_tmap.getInorderKeys() == ["Jordan", "Messi", "Ronaldo"]
# new_tmap.remove("Jordan")
# assert new_tmap.getInorderKeys() == ["Messi", "Ronaldo"]
# new_tmap.remove("Messi")
# assert new_tmap.getInorderKeys() == ["Ronaldo"]
# new_tmap.remove("Ronaldo")
# assert new_tmap.getInorderKeys() == []
