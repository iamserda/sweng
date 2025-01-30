# Convert Roman Numerals to Integer

## Intuition
The conversion of Roman numerals to integers is a classic problem that requires understanding the Roman numeral system's rules. In this system, numbers are represented by combinations of letters from the Latin alphabet. Each letter has a fixed integer value, and the placement of a smaller value before a larger value indicates subtraction. The challenge lies in correctly applying these rules to derive the numerical value from the Roman numeral string representation.

## Approach
The solution involves iterating through the string of Roman numerals and converting each symbol to its corresponding integer value. The key steps are as follows:
- **Mapping Roman Numerals to Integers**: A dictionary (`roman_int_val`) maps each Roman numeral character to its integer value.
- **Iterating Through the String**: For each character in the Roman numeral string:
  - If it's the first character, simply add its value to an array (`int_arr`).
  - For subsequent characters, compare the value of the current character (`current_char_int`) with the value of the previous character (`prev_char_int`):
    - If `prev_char_int` is less than `current_char_int`, it indicates a subtraction scenario (e.g., IV or IX). Subtract `prev_char_int` from `current_char_int`, remove the last value from `int_arr` (which was `prev_char_int`), and add the result to `int_arr`.
    - Otherwise, add `current_char_int` to `int_arr`.
- **Summing Up**: The integer value of the Roman numeral string is the sum of the integers in `int_arr`.

## Complexity
- **Time Complexity**: $$O(n)$$ - The algorithm iterates through the string once, where `n` is the length of the string. The operations within each iteration are constant time.
- **Space Complexity**: $$O(n)$$ - The space complexity is linear with respect to the length of the input string due to the storage of each character's integer value in `int_arr`.

## Code
```python
def roman_to_int(str_: str) -> int:
    roman_int_val = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000,
    }
    int_arr = []
    for index, char in enumerate(str_):
        if index == 0:
            int_arr.append(roman_int_val[char])
        else:
            prev_char_int = int_arr[-1]
            current_char_int = roman_int_val[char]
            if prev_char_int < current_char_int:
                int_arr.append(current_char_int - int_arr.pop())
            else:
                int_arr.append(current_char_int)
    return sum(int_arr)

# Example usage
print(roman_to_int("MCMXCIV"))  # Output: 1994
print(roman_to_int("LVIII"))    # Output: 58
print(roman_to_int("III"))      # Output: 3
```

## Remarks
This solution elegantly addresses the problem of converting Roman numerals to integers by leveraging the rules of the Roman numeral system and applying them through a straightforward iterative approach. It showcases the importance of understanding the problem domain and translating that understanding into an efficient algorithm.

### Credit, Source, Etc
- This implementation is designed as a practical and educational tool for understanding both the Roman numeral system and the application of basic algorithmic strategies in solving conversion problems.
- The simplicity and efficiency of the approach make it suitable for a wide range of applications, from educational purposes to practical use cases requiring Roman numeral conversion.

### Credit, Source, Etc...

- Source: [LeetCode](https://leetcode.com/problems/concatenation-of-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
