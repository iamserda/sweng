# [Baseball Game](https://leetcode.com/problems/baseball-game/description/)

## Intuition
When first encountering the problem, the key seems to be interpreting and applying a series of operations to calculate a score. The operations are symbolic, representing adding a new score, doubling a score, removing a score, or summing the last two scores. The challenge is effectively managing these operations in sequence to maintain an accurate running total.

## Approach
The solution uses a list named `score` to keep track of the points after each operation. By iterating through the list of operations:
- When encountering "C", the last score is removed (`pop`).
- For "D", the last score is doubled and added to the list. This requires temporarily removing the last score with `pop`, doubling it, then adding both the original and doubled scores back.
- The "+" operation sums the last two scores and adds this sum to the list. This involves popping the last two scores to calculate their sum, then putting them back along with their sum.
- If the operation is a number (represented by `item` in the `match` case), it's converted to an integer and added to the list.
The sum of the final list represents the total score.

## Complexity
- Time complexity: $$O(n)$$

  The solution involves a single pass through the operations list, with each operation requiring constant time, resulting in linear time complexity. Note that the `pop` and `append` operations on the list are also O(1).

- Space complexity: $$O(n)$$

  The extra space used by the solution is for the `score` list, which in the worst case might need to store a number for each operation, thus leading to a linear space complexity with respect to the number of operations.

## Code

```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for item in operations:
            match item:
                case "C":
                        score.pop()
                case "D":
                        value = score.pop()
                        score.append(value)
                        score.append(value * 2)
                case "+":
                    if len(score) >= 2:
                        item1 = score.pop()
                        item2 = score.pop()
                        item3 = item1 + item2
                        score.append(item2)
                        score.append(item1)
                        score.append(item3)
                case _:
                    score.append(int(item))
        return sum(score)
```

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/baseball-game/description/)
- [GitHub: @iamserda](https://github.com/iamserda)
- [Twitter: @iamserda](https://twitter.com/iamserda)
- [LinkedIn: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in NYC by [@iamserda](https://www.twitter.com/iamserda)