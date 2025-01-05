# [86. Partition List](https://leetcode.com/problems/partition-list/description/)

## Intuition
Given a singly linked list and a value `x`, the task is to partition the list such that all nodes less than `x` come before nodes greater than or equal to `x` without changing the original order of the nodes. The intuitive approach is to create two separate lists: one for elements less than `x` (`pre_list`) and another for elements greater than or equal to `x` (`post_list`), and then merge these lists.

## Approach
The solution involves iterating through the original list and distributing nodes into two new lists based on their value relative to `x`:
- **Initialization**: Start with two pairs of pointers, `pre_head` and `pre_tail` for the `pre_list`, and `post_head` and `post_tail` for the `post_list`. These pointers help in building the two lists efficiently.
- **Iteration**: Traverse the original list. For each node:
  - Detach the current node from the list (to avoid unintended side effects) by setting `current.next` to `None`.
  - If the node's value is less than `x`, append it to the end of the `pre_list`. If `pre_list` is empty, initialize it with the current node.
  - Otherwise, append the node to the `post_list` with similar logic.
- **Merging**: After the iteration, connect the `pre_list` and `post_list`. If `pre_list` is not empty, its tail (`pre_tail.next`) should point to the head of `post_list` to merge them. Return `pre_head` as the new head of the merged list.
- If `pre_list` is empty, the merged list is just the `post_list`, so return `post_head`.

## Complexity
- **Time Complexity**: $$O(n)$$ - The algorithm iterates through the list exactly once, where `n` is the number of nodes in the list.
- **Space Complexity**: $$O(1)$$ - The space used does not depend on the size of the input list. The algorithm only uses a fixed number of pointers (head and tail pointers for two lists) and does not allocate any additional nodes.

## Code
```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    # Initialize heads and tails for two lists
    pre_head = pre_tail = post_head = post_tail = None
    
    current = head
    while current:
        next_node = current.next  # Save next node
        current.next = None  # Break the link to ensure clean partitioning
        
        if current.val < x:
            if not pre_head:  # Initialize pre list
                pre_head = pre_tail = current
            else:
                pre_tail.next = current
                pre_tail = current
        else:
            if not post_head:  # Initialize post list
                post_head = post_tail = current
            else:
                post_tail.next = current
                post_tail = current
                
        current = next_node  # Move to the next node
    
    # Connect the two lists
    if pre_tail:
        pre_tail.next = post_head
        return pre_head
    else:
        return post_head

```

### Credit, Source, Etc
- This solution exemplifies a straightforward yet effective way to manipulate linked lists based on node values, maintaining order and achieving partition with minimal space overhead.
- Designed for educational purposes, this function showcases foundational concepts in linked list manipulation and algorithm design, emphasizing logical partitioning and efficient list operations.

- Source: [LeetCode](https://leetcode.com/problems/partition-list/description/)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
