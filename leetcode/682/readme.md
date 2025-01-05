# [Baseball Game](https://leetcode.com/problems/baseball-game/description/)

**Difficulty:**Easy

**Topics:**Array, Stack

## Companies

This problem may be encountered in interviews at companies that focus on data structures, such as tech startups, mid-sized companies, and large tech companies like Google, Amazon, and Facebook.

## Description

You are tasked with keeping score for a baseball game with unconventional rules. Initially, the game starts with an empty record.

You are given a list of strings `ops`, where `ops[i]` represents the ith operation you must apply to the record. The operations are as follows:

- An integer `x` - Record a new score of `x`.
- `'+'` - Record a new score that is the sum of the previous two scores.
- `'D'` - Record a new score that is double the previous score.
- `'C'` - Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

### Examples

**Example 1:**

- Input: `ops = ["5","2","C","D","+"]`
- Output: `30`
- Explanation:
  - `"5"` - Add 5 to the record, record is now [5].
  - `"2"` - Add 2 to the record, record is now [5, 2].
  - `"C"` - Invalidate and remove the previous score, record is now [5].
  - `"D"` - Add 2 * 5 = 10 to the record, record is now [5, 10].
  - `"+"` - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
  - The total sum is 5 + 10 + 15 = 30.

**Example 2:**

- Input: `ops = ["5","-2","4","C","D","9","+","+"]`
- Output: `27`
- Explanation:
  - Operations proceed as described in the example, resulting in a final record and a total sum of 27.

**Example 3:**

- Input: `ops = ["1","C"]`
- Output: `0`
- Explanation:
  - `"1"` - Add 1 to the record, record is now [1].
  - `"C"` - Invalidate and remove the previous score, record is now [].
  - Since the record is empty, the total sum is 0.

### Constraints

- `1 <= operations.length <= 1000`
- `operations[i]` is "C", "D", "+", or a string representing an integer in the range `[-3 * 10^4, 3 * 10^4]`.
- For operation `"+"`, there will always be at least two previous scores on the record.
- For operations `"C"` and `"D"`, there will always be at least one previous score on the record.

## Approach

To solve this problem, you can use a stack to keep track of the scores. Iterate through each operation and apply the following logic based on the operation type:

- If the operation is an integer, push it onto the stack.
- If the operation is `"C"`, pop the last score from the stack.
- If the operation is `"D"`, push onto the stack twice the last score.
- If the operation is `"+"`, push onto the stack the sum of the last two scores.

Finally, sum all elements in the stack to get the total score. This approach efficiently handles the operations and maintains the scores' history to calculate the total sum.


### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/baseball-game/description/)
- [GitHub: @iamserda](https://github.com/iamserda)
- [Twitter: @iamserda](https://twitter.com/iamserda)
- [LinkedIn: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in NYC by [@iamserda](https://www.twitter.com/iamserda)
