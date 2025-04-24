# [1399. Count Largest Group](https://leetcode.com/problems/count-largest-group/description/)

## Intuition
The problem asks us to group numbers from 1 to `n` based on the **sum of their digits**, then return how many groups share the largest size. Instinctively, this is a classic case of bucketing: we compute a key (digit sum), increment its count, and finally find the size of the largest bucket and how many buckets have that size.

## Approach
- Iterate from 1 through `n`.
- For each number, compute the **digit sum** (e.g., `123` → `1 + 2 + 3 = 6`).
- Use a dictionary (`defaultdict`) to group counts by this digit sum.
- Once all numbers are grouped, determine:
  - The **maximum size** of all groups.
  - The **count** of groups having that maximum size.

The core trick lies in how we compute digit sums and efficiently group sizes using `collections.defaultdict`.

## Complexity
- **Time complexity**: $$O(n \cdot d)$$, where $$d$$ is the average number of digits in numbers from 1 to $$n$$. Since $$d \approx \log_{10}(n)$$, the overall time is effectively linear for practical values of $$n$$.
- **Space complexity**: $$O(k)$$, where $$k$$ is the number of possible digit sums. For `n <= 10000`, the digit sum can't exceed `9*5=45`, so at most 46 buckets.

## Code
```python
from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sum_groups = defaultdict(int)

        for number in range(1, n + 1):
            digit_sum = sum(int(digit) for digit in str(number))
            digit_sum_groups[digit_sum] += 1

        max_size = max(digit_sum_groups.values())
        return sum(1 for group_size in digit_sum_groups.values() if group_size == max_size)
```

## Example
```plaintext
Input: n = 13
Groups:
{1, 10} → sum = 1
{2, 11} → sum = 2
{3, 12} → sum = 3
{4, 13} → sum = 4
{5}
{6}
{7}
{8}
{9}
Output: 4 (groups with size = 2)
```

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/count-largest-group/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
