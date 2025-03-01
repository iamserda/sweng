class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(4)

head2 = Node(1)
head2.next = Node(3)
head2.next.next = Node(5)

head3 = Node(3)
head3.next = Node(6)

list1 = [head1, head2, head3]


def merge_linked_list(head1, head2):
    curr1 = head1
    curr2 = head2
    head3 = Node(1)
    curr3 = head3
    while curr1 or curr2:
        if not curr1:
            curr3.next = curr2
            break

        if not curr2:
            curr3.next = curr1
            break

        if curr1.value <= curr2.value:
            curr3.next = curr1
            curr1 = curr1.next
            curr3 = curr3.next
            curr3.next = None
            continue

        if curr1.value > curr2.value:
            curr3.next = curr2
            curr2 = curr2.next
            curr3 = curr3.next
            curr3.next = None
            continue

    return head3.next


def convert_to_list(head):
    curr = head
    arr = []
    while curr:
        arr.append(curr.value)
        curr = curr.next
    return arr


while len(list1) > 1:
    ll1 = list1.pop()
    ll2 = list1.pop()
    print(convert_to_list(ll1))
    print(convert_to_list(ll2))
    h3 = merge_linked_list(ll1, ll2)
    print(convert_to_list(h3))
    list1.append(h3)
