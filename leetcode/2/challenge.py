import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def to_arr(self, li):
        arr = []
        temp = li
        while temp:
            arr.append(temp.val)
            temp = temp.next
        return arr

    def to_number(self, li):
        temp = li
        arr = []
        while temp:
            arr.append(str(temp.val))
            temp = temp.next
        L = 0
        R = len(arr) - 1
        while L <= R:
            arr[L], arr[R] = arr[R], arr[L]
            L += 1
            R -= 1
        print(arr)
        return int("".join(arr))

    def list_generator(self):
        head = ListNode("pre")
        arr = [ListNode(random.randint(0, 9)) for i in range(random.randint(1, 9))]
        pre = head
        for elem in arr:
            pre.next = elem
            pre = pre.next
        return head.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Start Here
        pass


# Testing Arena:
sol = Solution()
l1 = sol.list_generator()
l2 = sol.list_generator()
l3 = sol.addTwoNumbers(l1, l2)
num1 = sol.to_number(l1)
num2 = sol.to_number(l2)
num3 = sol.to_number(l3)
print(f"{num1} + {num2} = {num3}")
assert num1 + num2 == num3
