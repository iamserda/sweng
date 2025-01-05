# [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

## Intuition

Upon encountering the problem of detecting a cycle in a linked list, my initial thought gravitates towards the challenge of identifying a repeating pattern without the use of extra space for tracking visited nodes. Traditional approaches might involve using a hash table to keep track of visited nodes, but this increases space complexity. Instead, an efficient and elegant solution can be achieved through the two-pointer technique, specifically the "tortoise and the hare" strategy, which intuitively suggests that if a cycle exists, a faster-moving pointer will eventually "lap" a slower-moving pointer.

## Approach

The implemented solution adopts the two-pointer technique, deploying a `fast` pointer that moves at double the speed of a `slow` pointer. Both pointers start at the head of the list. The algorithm progresses by incrementing the `slow` pointer by one step and the `fast` pointer by two steps in each iteration. If the linked list has a cycle, these pointers will meet at some point, indicating the presence of a cycle. Conversely, if the list is acyclic, the `fast` pointer will reach the end of the list (`null`), and the loop will terminate, signaling the absence of a cycle.

## Complexity

- Time complexity: $$O(n)$$

  In the worst-case scenario, the time complexity is linear relative to the number of nodes in the list. This accounts for the situation where the fast pointer traverses the entire list without encountering a cycle or meets the slow pointer just before it completes the cycle.

- Space complexity: $$O(1)$$

  The space complexity is constant as the solution employs only two pointers regardless of the size of the input linked list, ensuring an efficient use of memory.

## Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from node import Node
from linkedlist import LinkedList


def has_cycle(head):
    """
        :type head: ListNode
        :rtype: bool
        """
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Testing Arenas:
# TEST 1
myLL = LinkedList(3)
myLL.append(2)
myLL.append(0)
myLL.append(-4)
myLL.tail.next = myLL.get(1)  # creating cyclical-link
assert has_cycle(myLL.head) is True
# TEST 2
myLL = LinkedList(3)
myLL.append(2)
myLL.append(0)
myLL.append(-4)
assert has_cycle(myLL.head) is False

# TEST 3
myLL = LinkedList(1)
myLL.append(2)
myLL.tail.next = myLL.get(0)
assert has_cycle(myLL.head) is True

# TEST 4
myLL = LinkedList(1)
assert has_cycle(myLL.head) is False

```

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/linked-list-cycle/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
