# 690. [Employee Importance](https://leetcode.com/problems/employee-importance/)

## Description

You are given a data structure of employee information, which includes the unique ID of each employee, their importance value, and the IDs of their direct subordinates.

Given an array of employees, `employees`, and an integer `id` representing the ID of an employee, return the total importance value of this employee and all their subordinates.

## Examples

**Example 1:**

Input:  
`employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], id = 1`  
Output: `11`  
Reasoning: Employee 1 has importance 5, and has two direct subordinates: 2 and 3. Each has importance 3. Total = 5 + 3 + 3 = 11.

**Example 2:**

Input:  
`employees = [[1, 2, [5]], [5, 3, []]], id = 5`  
Output: `3`  
Reasoning: Employee 5 has importance 3 and no subordinates.

## Constraints

- `1 <= employees.length <= 2000`
- `1 <= employees[i].id <= 2000`
- All `employees[i].id` are unique.
- `employees[i].importance` is in the range `[1, 100]`.
- `employees[i].subordinates.length <= 10`
- You can assume that all IDs in `employees[i].subordinates` are valid and exist in `employees`.

**Follow-up:**  
Can you solve this problem using DFS or BFS?

## Credits, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/employee-importance/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

