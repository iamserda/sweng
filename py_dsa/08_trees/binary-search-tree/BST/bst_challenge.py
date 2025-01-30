"""Implement the following: BinarySearchTree class."""
# class BinarySearchTree:

# TESTING ARENAS:
my_bst = BinarySearchTree()
arr = [20,10,30,5,15,25,35,2,8,12,18,22,26,33,40,1,3,11,13,17,19,21,23,24,28,31,39,38,41]
for ar in arr:
    my_bst.insert(ar)

print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.left.left.value)
print(my_bst.root.left.right.value)
print(my_bst.root.right.value)
print(my_bst.root.right.left.value)
print(my_bst.root.right.right.value)

assert my_bst.search(40) is True
assert my_bst.search(41) is True
assert my_bst.search(42) is False