# [1836. Remove Duplicates From an Unsorted Linked List](https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/description/)


## Intuition
Confronted with the challenge of removing duplicate nodes from an unsorted linked list, the instinctive approach is to track occurrences of each value as the list is traversed. The goal is to retain only nodes with unique values while ensuring the original order of these unique nodes is preserved.

## Approach
The provided solution employs a two-pass strategy using a hash table to count occurrences of each node's value:
- **First Pass**: Traverse the list once to populate a hash table (`hash_counter`) with the count of each value.
- **Second Pass**: Traverse the list again, this time removing nodes whose values appear more than once in the hash table.
- A dummy node (`node` with value 0) is utilized at the beginning to simplify edge case handling, particularly when the head of the list needs to be removed.
- The `pre` pointer is used to keep track of the last node in the list that is guaranteed to be kept, facilitating the removal of nodes directly by adjusting `pre.next`.

## Complexity
- **Time Complexity**: $$O(N)$$ - The list is traversed twice, where $$N$$ is the number of nodes in the list. The first traversal is for counting occurrences, and the second is for removing duplicates, each taking linear time.
- **Space Complexity**: $$O(N)$$ - The hash table `hash_counter` stores a count for each unique value in the list, which in the worst case (all unique values) requires space proportional to the number of nodes in the list.

## Code
The implementation details are encapsulated within two primary functions:
- `deleteDuplicatesUnsorted` for removing duplicate nodes based on the described approach.
- `linkedlist_to_arr` for converting the linked list back to an array for easy testing and verification of results.

```python
class Node:
    """Node class with constructor"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicatesUnsorted(head: Node) -> Node:
    """Given the head of a linked list, find all the values that appear more 
    than once in the list and delete the nodes that have any of those values. 
    Return the linked list after the deletions."""
    if not head:
        return
    if not head.next:
        return head

    node = Node(0)
    node.next = head
    temp = head
    hash_counter = {}

    while temp:
        if temp.val not in hash_counter:
            hash_counter[temp.val] = 1
        else:
            hash_counter[temp.val] += 1
        temp = temp.next

    pre = node
    temp = head
    while temp:
        if hash_counter[temp.val] == 1:
            pre = temp
            temp = temp.next
        else:
            pre.next = temp.next
            temp.next = None
            temp = pre.next

    head = node.next
    node.next = None
    return head
```

## Testing
The solution is verified with two test cases, demonstrating its ability to handle both the presence and absence of duplicates:
- **Test 0**: Successfully removes duplicates `[3, 2]` from the list, leaving `[4, 5]`.
- **Test 1**: With no duplicates, the list remains unchanged `[3, 4, 5, 1, 2, 0]`.
- **Note on Test 2**: This test appears to misunderstand the expected output, merely converting a list to an array without applying `deleteDuplicatesUnsorted`. However, the inclusion and description suggest an oversight rather than a test of functionality.

### Credit, Source, Etc
- This solution showcases efficient manipulation of linked lists to remove duplicates without sorting, leveraging hash tables for quick lookups.
- The testing framework demonstrates the function's effectiveness and correctness across various scenarios.

Crafted with the aim of enhancing understanding of linked list operations and hash table applications, this solution exemplifies key algorithm design principles necessary for efficient data structure manipulation.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/description/)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
