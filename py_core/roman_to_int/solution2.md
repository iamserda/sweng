## Improved Solution for Converting Roman Numerals to Integers

While the original solution for converting Roman numerals to integers is efficient in terms of time complexity, operating in $$O(n)$$ where $$n$$ is the length of the string (which is optimal for this problem as each character needs to be examined), there's little room for improvement in time complexity. However, the space complexity and the overall implementation can be made slightly more efficient and cleaner.

### Approach
Instead of using an additional array to store intermediate values, we can directly accumulate the result in an integer variable. This approach reduces space complexity by avoiding unnecessary storage.

- **Direct Accumulation**: Iterate through the string of Roman numerals in reverse order, adding the value of each numeral to a running total. If a numeral is less than the numeral immediately to its right, subtract its value instead of adding it. This change eliminates the need for an additional array and directly computes the final integer value.

### Complexity
- **Time Complexity**: $$O(n)$$ - The solution still requires a single pass through the string, examining each character exactly once.
- **Space Complexity**: $$O(1)$$ - This approach uses a fixed amount of space regardless of the input size, improving on the original solution's linear space usage.

### Improved Code
```python
def roman_to_int(str_: str) -> int:
    roman_int_val = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000,
    }
    total = 0
    prev_value = 0
    for char in reversed(str_):
        current_value = roman_int_val[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    return total

# Example usage
print(roman_to_int("MCMXCIV"))  # Output: 1994
print(roman_to_int("LVIII"))    # Output: 58
print(roman_to_int("III"))      # Output: 3
```

### Remarks
By directly accumulating the integer value and iterating in reverse, this improved solution maintains the original's efficiency while enhancing its space efficiency and simplifying the logic. It demonstrates how understanding the problem's nuances allows for optimizations that maintain or improve algorithmic performance.

### Credit, Source, Etc
- This refinement builds on the foundational approach to Roman numeral conversion, focusing on optimizing resource usage and simplifying the implementation.
- Tailored for both educational and practical applications, this improved solution underscores the importance of algorithmic efficiency and resource-conscious programming.

### Credit, Source, Etc...

- Source: [LeetCode](https://leetcode.com/problems/concatenation-of-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)