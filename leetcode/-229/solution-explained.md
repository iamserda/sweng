# [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/description/)

## Intuition
The task of reversing the words in a string, while maintaining their original order, made me think about the importance of identifying word boundaries and handling spaces correctly. It seemed clear that iterating through the string from the end and building words character by character could efficiently achieve the goal. Additionally, reversing each word as it's constructed before adding it to the result would address the need to maintain the original word order.

## Approach
The approach taken involves iterating over the input string in reverse. This allows for the easy identification of word boundaries (spaces) and the construction of words from the end to the start. Here's a step-by-step breakdown:
- **Initialization**: A temporary word holder (`word`) collects characters until a space is encountered, indicating a word boundary. An array (`result_array`) gathers the reversed words.
- **Iteration**: By traversing the string backward, each character is examined:
  - If a space is encountered and the `word` holder contains characters, this indicates the end of a word. The word is then reversed and added to the `result_array`.
  - If a character is not a space, it's added to the `word` holder for later reversal.
  - At the start of the string (`str_index == 0`), any remaining characters in the `word` holder are treated as the last word, reversed, and added to `result_array`.
- **Result Construction**: The `result_array`, which now contains reversed words in their original order, is joined into a single string with spaces and returned.

## Complexity
- **Time complexity**: $$O(n)$$, where $$n$$ is the length of the input string. Each character in the input string is visited exactly once during the iteration. Additionally, reversing each word also takes linear time relative to its length, but since all words collectively form the input string, the overall time complexity remains linear.
- **Space complexity**: $$O(n)$$, as additional storage is required for the `word` holder and the `result_array`. In the worst case, where all characters are unique words, the space required to store these words would be linearly proportional to the length of the input string.

## Code
```python
class Solution:        
    def reverseWords(self, s: str) -> str:
        word = ""
        result_array = []
        for str_index in range(len(s)-1, -1, -1):
            if s[str_index] == " ":
                if word:
                    # Reverse the accumulated word and append it to the result array
                    result_array.append(word[::-1])
                word = ""
            else:
                word += s[str_index]
            if str_index == 0 and word:
                # Reverse the last word and append it to the result array
                result_array.append(word[::-1])
        return " ".join(result_array)
```

This refined solution simplifies the reversal of each word by using Python's slice notation (`word[::-1]`) for a more concise and efficient reversal process, enhancing readability and maintaining the original approach's efficiency.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)