# 875. [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

## Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i`th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses a pile and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and won't eat any more bananas during that hour.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Examples

**Example 1:**

Input: `piles = [3,6,7,11], h = 8`  
Output: `4`  
Reasoning: At speed 4, she eats [3, 6, 7, 11] in [1, 2, 2, 3] hours = 8 hours.

**Example 2:**

Input: `piles = [30,11,23,4,20], h = 5`  
Output: `30`

**Example 3:**

Input: `piles = [30,11,23,4,20], h = 6`  
Output: `23`

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

**Follow-up:**  
Can you solve the problem with an algorithm faster than O(n log max(piles)) where n is the number of piles?

## Credits, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/koko-eating-bananas/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
