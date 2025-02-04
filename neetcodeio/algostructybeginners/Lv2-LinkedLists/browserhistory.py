"""
title: 1472. Design Browser History
url: https://leetcode.com/problems/design-browser-history/description/
owner: leetcode.com
desicription: solution using a doubly linked list
solver: @iamserda
"""

class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.tail = self.head

    def visit(self, url: str) -> None:
        new_url = Node(url)
        if self.tail:
            if self.tail.next:
                self.tail.next.prv = None
            self.tail.next = new_url
            new_url.prev = self.tail
            self.tail = self.tail.next
        else:
            self.head = new_url
            self.tail = new_url

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.tail and self.tail.prev:
                self.tail = self.tail.prev
                continue
        return self.tail.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.tail and self.tail.next:
                self.tail = self.tail.next
                continue
        return self.tail.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
