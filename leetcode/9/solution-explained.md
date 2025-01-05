# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## Intuition

When presented with the problem of determining whether an integer is a palindrome, my initial thought was to leverage the symmetry of palindromes. Since a palindrome reads the same backward as forward, comparing the digits from the ends towards the middle should verify this property without needing to convert the integer into a different data structure or manipulate it as a string.

## Approach

The solution employs a straightforward method:
- **Negative Check**: Immediately return `False` for any negative integer, as negative signs disrupt palindrome symmetry.
- **Digit Extraction**: Decompose the integer into its constituent digits by repeatedly taking the modulo (`%`) of 10 to get the last digit and then dividing by 10 (using integer division `//`) to remove that digit. Each extracted digit is stored in an array.
- **Two-Pointer Technique**: Initialize two pointers at the start and end of the array. Incrementally move them towards the center, comparing the digits they point to at each step. If any pair of digits differ, the number cannot be a palindrome.
- **Result**: If all corresponding digits match, return `True`, indicating the number is a palindrome.

## Complexity

- **Time complexity**: $$O(n)$$, where $$n$$ is the number of digits in the integer. The while loop for digit extraction iterates once per digit, and the subsequent comparison also operates in linear time relative to the number of digits.
- **Space complexity**: $$O(n)$$, due to storing each digit of the integer in an array for comparison. The space required is directly proportional to the number of digits in the input integer.

## Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_ = x
        arr = []
        while x_ > 0:
            arr.append(x_ % 10)
            x_ //= 10
        
        start = 0
        end = len(arr) - 1
        while start <= end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True
```

This implementation effectively determines whether an integer is a palindrome by comparing its digits, adhering to the constraints and properties of palindromes without converting the integer into a string or employing additional data structures beyond the array for digit storage.

### Credit, Source, Etc

- Source: [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)