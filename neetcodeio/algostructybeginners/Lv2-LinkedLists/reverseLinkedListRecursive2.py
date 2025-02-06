class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseList(head: Node):
    if head is None:
        raise TypeError("Expected a Node, received NoneType!")

    if head.next is None:
        return head, None
    else:
        new_head, new_tail = reverseList(head.next)
        head.next = None
        if new_tail is None:
            # print(new_head.data, new_tail)
            new_head.next = head
            new_tail = new_head.next
        else:
            # print(new_head.data, new_tail.data)
            new_tail.next = head
            new_tail = new_tail.next
        return new_head, new_tail


def list_to_arr(head, arr):
    temp = head
    while temp:
        print(temp.data)
        arr.append(temp.data)
        temp = temp.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
before = []
list_to_arr(head, before)
print(before)

after = []
_head, _tail = reverseList(head)
list_to_arr(_head, after)
print(after)
