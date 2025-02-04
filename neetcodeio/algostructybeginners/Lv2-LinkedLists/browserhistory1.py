"""
title: 1472. Design Browser History
url: https://leetcode.com/problems/design-browser-history/description/
owner: leetcode.com
desicription: Solution with two stacks
solver: @iamserda
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.prev = [homepage]
        self.next = []

    def visit(self, url: str) -> None:
        self.prev.append(url)
        self.next = []

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.prev:
                self.next.append(self.prev.pop())
        if not self.prev:
            self.prev.append(self.next.pop())
        return self.prev[-1]

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.next:
                self.prev.append(self.next.pop())
        return self.prev[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
