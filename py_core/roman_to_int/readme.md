# Convert Integer to Roman Numerals

## Difficulty

Medium

## Topics

- Math
- String

## Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D`, and `M`. Given an integer, convert it to a Roman numeral.

The Roman numerals are constructed following these rules:

1. The numbers `1`, `2`, and `3` are represented by `I`, `II`, and `III`, respectively.
2. The number `4` is represented as `IV`, `5` as `V`, `9` as `IX`, `10` as `X`, `40` as `XL`, `50` as `L`, `90` as `XC`, `100` as `C`, `400` as `CD`, `500` as `D`, `900` as `CM`, and `1000` as `M`.
3. Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five, we subtract it, making four. The same principle applies to the number nine, which is written as `IX`.
4. There are six instances where subtraction is used: `IV` (4), `IX` (9), `XL` (40), `XC` (90), `CD` (400), and `CM` (900).

### Examples

**Example 1:**

- Input: `num = 3`
- Output: `"III"`
- Explanation: `3` is represented as `3` ones.

**Example 2:**

- Input: `num = 58`
- Output: `"LVIII"`
- Explanation: `L = 50`, `V = 5`, `III = 3`.

**Example 3:**

- Input: `num = 1994`
- Output: `"MCMXCIV"`
- Explanation: `M = 1000`, `CM = 900`, `XC = 90`, `IV = 4`.

### Constraints

- `1 <= num <= 3999`

## Approach

To convert an integer to a Roman numeral, you can follow a greedy approach. Start with the largest possible Roman numeral (`M` for 1000) and subtract it from your number, appending the corresponding numeral to your result string each time the subtraction is possible. Repeat this process, working your way down through the Roman numeral values (`CM`, `D`, `CD`, `C`, `XC`, `L`, `XL`, `X`, `IX`, `V`, `IV`, `I`), until the entire integer has been converted.

This approach ensures that you always use the largest numeral possible for each part of the integer, which is the key to forming correct Roman numerals.


### Credit, Source, Etc...

- Source: [LeetCode](https://leetcode.com/problems/concatenation-of-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)