# [1598. Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder/description)

## Intuition
Given a series of operations represented by strings in an array, where each operation takes us deeper into a nested folder structure, returns us to the parent folder, or keeps us in the current folder, the challenge is to compute the minimum number of operations needed to return to the main folder. The operations are intuitive: moving into a new folder, stepping back to the parent folder, or staying in the current folder. The task essentially simulates navigating a file system.

## Approach
The `Solution` class uses a stack to model the folder structure and operations:
- **Initialization**: Sets up an empty stack and a length variable to track the stack's size.
- **`minOperations` Method**:
  - Iterates through the list of operations.
  - For each operation:
    - If the operation is "../", and the stack is not empty, it pops the last operation off the stack and decrements the length, simulating a return to the parent folder.
    - If the operation is "./", it does nothing, as this represents staying in the current folder.
    - For any other operation, it simulates moving into a new folder by pushing the operation onto the stack and incrementing the length.
  - Returns the length of the stack, which represents the depth from the main folder after all operations have been applied.

## Complexity
- **Time Complexity**: $$O(n)$$ - Iterates through each operation in the list once, where `n` is the number of operations. The operations on the stack (push and pop) are $$O(1)$$, leading to a linear time complexity.
- **Space Complexity**: $$O(n)$$ - In the worst case, if all operations are moving into new folders, the stack could grow to size `n`, where `n` is the number of operations.

## Code
```python
class Solution:
    def __init__(self):
        self.stack = []
        self.length = 0

    def minOperations(self, logs: List[str]) -> int:
        for op in logs:
            if op == "../":
                if self.length > 0:
                    self.stack.pop()
                    self.length -= 1
            elif op == "./":
                continue
            else:
                self.stack.append(op)
                self.length += 1
        return self.length
```

### Credit, Source, Etc
- This solution models a basic file navigation system, utilizing stack operations to efficiently simulate the process of moving through a folder structure based on a series of string commands.
- Designed to provide a straightforward and intuitive approach to solving problems involving simulated navigation or path tracking in a constrained environment.

Crafted with attention to clarity and efficiency, this solution aims to offer a practical understanding of how to apply stack data structures to solve problems related to path navigation and operation sequencing.

- Source: [LeetCode](https://leetcode.com/problems/crawler-log-folder/description)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
