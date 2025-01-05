from node import Node
from linkedlist import LinkedList


def reverse_LinkedList(head):
    if not head:
        return None
    if not head.next:
        return head
    left_ptr = None
    temp_ptr = head
    right_ptr = temp_ptr
    while temp_ptr:
        right_ptr = right_ptr.next
        temp_ptr.next = left_ptr
        left_ptr = temp_ptr
        temp_ptr = right_ptr
    head = left_ptr
    return head


def convert_to_list(head):
    if head:
        temp = head
        my_list = []
        while temp:
            my_list.append(temp.value)
            temp = temp.next
        return my_list


my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)

arr = convert_to_list(my_linked_list.head)
print("pre-reversal:", arr)
temp_head = reverse_LinkedList(my_linked_list.head)
arr = convert_to_list(temp_head)
print("post-reversal:", arr)
