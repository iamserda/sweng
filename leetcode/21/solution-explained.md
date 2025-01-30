# [21. Merge Two Sorted Lists](https://leetcode.com/problems/crawler-log-folder/description)

## Problem Statement
Given the heads of two sorted linked lists `list1` and `list2`, merge the two lists into a single, sorted linked list. The merged list should be made by splicing together the nodes of the first two lists, and should also be sorted.

## Approach
The function `mergeTwoLists` takes two sorted linked lists and merges them into one sorted list. Here’s a step-by-step explanation:
- A temporary dummy node `new_list` is created to serve as the anchor for the new list, ensuring an easy way to return the head of the merged list at the end.
- A `tail` pointer is used to keep track of the last node in the merged list, starting with the dummy node.
- The function iterates through `list1` and `list2` as long as there are elements left in either list:
  - If one of the lists is exhausted, the `tail` is pointed to the remaining elements of the other list.
  - Otherwise, the nodes from `list1` and `list2` are compared, and the smaller one is appended to the merged list's tail, and `tail` is updated to this newly added node.
- After completing the iteration, the dummy node's `next` is returned, which points to the head of the merged list.

## Complexity Analysis
- **Time Complexity**: $$O(n + m)$$, where $$n$$ is the length of `list1` and $$m$$ is the length of `list2`. Each element in both lists is visited exactly once, making the algorithm linear with respect to the total number of elements in both lists.
- **Space Complexity**: $$O(1)$$, since the merge is done in-place by reusing the nodes of the given lists without allocating any additional nodes.

## Code
```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    new_list = Node(0)
    tail = new_list

    while list1 or list2:
        if not list1:
            tail.next = list2
            break
        elif not list2:
            tail.next = list1
            break
        elif list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    return new_list.next
```

## Testing
The solution includes a testing function `to_list`, which converts the linked list back into a Python list for easy verification:
- Initial linked lists `s1` and `s2` are created and verified against their expected list representations.
- The merged list `merged_linked` is tested to ensure it matches the expected merged list representation.

### Credit, Source, Etc
- This solution is a straightforward and efficient approach to a common problem encountered when manipulating linked lists, emphasizing the importance of pointer manipulation and iterative comparison.
- Inspired by LeetCode Problem 25, this algorithm is designed to provide clear insight into merging sorted data structures, a fundamental concept in algorithm design and data structure manipulation.

This implementation, crafted with care and precision, offers a solid foundation for understanding linked list operations and the merging of sorted sequences.

- Source: [LeetCode](https://leetcode.com/problems/crawler-log-folder/description)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
