# [1207. Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/description/)

## Intuition

Initially, the problem seems to involve counting the occurrences of each element in a given list and then determining if all these counts are unique. This suggests a need for a way to track each element's frequency and then verify the uniqueness of these frequencies without overlap.

## Approach

The solution involves two main steps. First, iterate through the input list, `arr`, and maintain a dictionary, `items_and_counts`, where each key-value pair corresponds to an element and its count of occurrences in the list. This step ensures that we have the frequency of each unique element.

In the second step, we iterate through the values of the `items_and_counts` dictionary to check if any frequency is repeated. This is done by trying to add each frequency to a set, `counts_set`. Sets inherently do not allow duplicate entries. If we encounter a frequency already present in the set, it indicates that at least two elements have the same number of occurrences, and we return `False`. If all frequencies are unique, the loop completes without finding duplicates, and we return `True`.

## Complexity

- **Time complexity:** The time complexity is $$O(n)$$ where $$n$$ is the number of elements in the input list `arr`. This is because we iterate through all elements once to count occurrences and then iterate through the unique counts, which in the worst case can be as large as the input list if all elements are unique.
- **Space complexity:** The space complexity is also $$O(n)$$, as in the worst case, the `items_and_counts` dictionary and the `counts_set` set combined could store information for each unique element in the input list, which would require space proportional to the number of elements in the list.

## Code

```python
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        items_and_counts = {}
        for item in arr:
            if item in items_and_counts:
                items_and_counts[item] += 1
                continue
            items_and_counts[item] = 1
        counts_set = set()
        for count in items_and_counts.values():
            if count in counts_set:
                return False
            counts_set.add(count)
        return True
```

This documentation covers the intuition behind the approach, the approach itself, and an analysis of the complexity of the solution, followed by the code implementation.

## Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
