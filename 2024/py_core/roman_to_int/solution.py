
def roman_to_int(str_: str) -> int:
    roman_int_val = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    int_arr = []
    for index, char in enumerate(str_):
        if index == 0:
            int_arr.append(roman_int_val[char])
            continue
        
        prev_char_int = int_arr[-1]
        current_char_int = roman_int_val[char]
        if prev_char_int < current_char_int:
            int_arr.append(current_char_int - int_arr.pop())
        else:
            int_arr.append(current_char_int)
    return sum(int_arr)

print(roman_to_int("MCMXCIV"))
i = roman_to_int('LVIII')
print(f"Welcome to SuperBowl LVIII({i})")
print(roman_to_int("III"))