# [1598. Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder/description)

**Difficulty:** Easy

**Topics:** Stack, String

## Companies

This problem may appear in interviews with companies that focus on file systems, web servers, or any system that navigates through a hierarchical structure, such as tech giants like Google, Amazon, or startups working with file management systems.

## Description

The Leetcode file system keeps a log each time a user performs a change folder operation. The operations are as follows:

- `"../"` : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
- `"./"` : Remain in the same folder.
- `"x/"` : Move to the child folder named x (This folder is guaranteed to always exist).

Given a list of strings `logs` where `logs[i]` is the operation performed by the user at the `i`th step, and the file system starts in the main folder, return the minimum number of operations needed to go back to the main folder after the change folder operations.

### Examples

**Example 1:**

- Input: `logs = ["d1/","d2/","../","d21/","./"]`
- Output: `2`
- Explanation: Use the change folder operation `"../"` 2 times to go back to the main folder.

**Example 2:**

- Input: `logs = ["d1/","d2/","./","d3/","../","d31/"]`
- Output: `3`

**Example 3:**

- Input: `logs = ["d1/","../","../","../"]`
- Output: `0`

### Constraints

- `1 <= logs.length <= 103`
- `2 <= logs[i].length <= 10`
- `logs[i]` contains lowercase English letters, digits, '.', and '/'.
- `logs[i]` follows the format described in the statement.
- Folder names consist of lowercase English letters and digits.

## Approach

To solve this problem, you can simulate the operations using a simple counter to track the depth of the current directory relative to the main folder:

- Initialize a counter `depth` to 0.
- Iterate through each operation in `logs`.
  - If the operation is `"../"` and `depth` is greater than 0, decrement `depth` by 1.
  - If the operation is `"x/"`, increment `depth` by 1.
  - Ignore operations that are `"./"` since they do not change the current directory level.
- Return the final value of `depth` as the minimum number of operations needed to return to the main folder.

This approach effectively calculates the minimum steps required to navigate back to the main folder by tracking the depth of directory changes.


### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/crawler-log-folder/description)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
