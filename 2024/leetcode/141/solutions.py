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
