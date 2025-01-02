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