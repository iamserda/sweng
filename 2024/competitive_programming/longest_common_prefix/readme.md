# LONGEST COMMON PREFIX

**Description:**
Create a function named `is_leap_year(year)` that takes an integer `year` as input and returns `True` if the given year is a leap year, and `False` otherwise.

A leap year is defined as follows:

- It is divisible by 4.
- If it is a century year (ends with 00), it must also be divisible by 400.

For example, 2000 and 2004 are leap years, but 1900 and 2003 are not.

**Your Task:**
Implement the `is_leap_year` function.

**Test Cases:**

1. `is_leap_year(2004)` should return `True`
2. `is_leap_year(2005)` should return `False`
3. `is_leap_year(2000)` should return `True`
4. `is_leap_year(1900)` should return `False`
5. `is_leap_year(2012)` should return `True`

**Expected Assertions:**

```python
assert is_leap_year(2004) == True
assert is_leap_year(2005) == False
assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2012) == True
```

Ensure your function passes all the test cases!
