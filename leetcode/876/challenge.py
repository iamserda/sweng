from linkedlist import LinkedList


def middle_node(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """


# Testing Arenas:
myLL = LinkedList(4)
myLL.append(5)
myLL.append(6)
myLL.append(8)
myLL.print_all_nodes()
print(middle_node(myLL.head))
