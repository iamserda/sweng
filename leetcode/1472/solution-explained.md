# [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/description)

## Intuition

Designing a browser history feature involves keeping track of the pages visited, allowing the user to go back and forward through the history. The initial thought is to use two stacks: one to keep track of the pages visited prior to the current page (for the back function) and another to keep track of the pages visited after the current page (for the forward function). This approach simulates the real-world behavior of a web browser's history navigation.

## Approach

The `BrowserHistory` class encapsulates this functionality with three main components:

- **Initialization**: Initializes with the `homepage`. Two lists, `backlog` and `fwd_log`, act as stacks to track the pages for backward and forward navigation, respectively. `current_page` stores the URL of the current page.
- **`visit` Method**: Simulates visiting a new page. The current page is pushed onto the `backlog` stack, the `current_page` is updated to the new URL, and the `fwd_log` is cleared since visiting a new page invalidates the forward history.
- **`back` Method**: Moves back in the history by the specified number of `steps`. It transfers pages from the `backlog` to the `fwd_log`, updating the `current_page` as it goes. If the `backlog` is exhausted, it stops moving back and returns the `current_page`.
- **`forward` Method**: Moves forward in the history by the specified number of `steps`, working similarly to the `back` method but transferring pages from the `fwd_log` back to the `backlog` and updating the `current_page` accordingly.

## Complexity

- **Time Complexity**:
  - For `visit`, it's $$O(1)$$ since it performs a constant number of operations.
  - For `back` and `forward`, it's $$O(steps)$$ in the worst case, where `steps` is the number of steps to move back or forward. This is because each step involves a constant number of operations (pop and push).
- **Space Complexity**: $$O(n)$$, where $$n$$ is the total number of pages visited. This is because the space needed is directly proportional to the number of pages stored in the `backlog` and `fwd_log`.

## Code 1

```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.backlog = []
        self.fwd_log = []
        self.current_page = homepage

    def visit(self, url: str) -> None:
        self.backlog.append(self.current_page)
        self.current_page = url
        self.fwd_log = []

    def back(self, steps: int) -> str:
        while steps > 0 and self.backlog:
            self.fwd_log.append(self.current_page)
            self.current_page = self.backlog.pop()
            steps -= 1
        return self.current_page

    def forward(self, steps: int) -> str:
        while steps > 0 and self.fwd_log:
            self.backlog.append(self.current_page)
            self.current_page = self.fwd_log.pop()
            steps -= 1
        return self.current_page
```

## Code 2

```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.backlog = []
        self.fwd_log = []
        self.current_page = homepage

    def visit(self, url: str) -> None:
        self.backlog.append(self.current_page)
        self.current_page = url
        self.fwd_log = []

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.backlog:
                return self.current_page
            self.fwd_log.append(self.current_page)
            self.current_page = self.backlog.pop()
        return self.current_page

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.fwd_log:
                return self.current_page
            self.backlog.append(self.current_page)
            self.current_page = self.fwd_log.pop()
        return self.current_page
```

### Credit, Source, Etc

- This solution is tailored for managing a simplified browser history, leveraging stack-based structures for efficient navigation through previously visited web pages.
- Focused on providing a clear and intuitive method for tracking and navigating web page history, the implementation demonstrates practical usage of data structures in software design.

Designed with simplicity and practicality in mind, the `BrowserHistory` class offers a foundational approach to understanding stack operations and their applications in managing sequential data, such as web browsing history.

- Source: [LeetCode](https://leetcode.com/problems/design-browser-history/description)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
