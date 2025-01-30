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

## Code-Walkthrough

### Code:
```python
class Solution:        
    def reverseWords(self, s: str) -> str:
        word = ""
        result_array = []
        "read the sentence backwards"
        for str_index in range(len(s)-1, -1, -1):
            # reversing word var and store each word
            if s[str_index] == " ":
                if len(word) > 0:
                    w = ""
                    for word_index in range(len(word)-1, -1, -1):
                        w += word[word_index]
                    result_array.append(w)
                word = ""
            else:
                word += s[str_index]
            
            # reversing any last word left
            if str_index == 0:
                if len(word) > 0:
                    stack1 = [w for w in word]
                    stack1_reversed = [stack1[i] for i in range(len(stack1)-1, -1, -1)]
                    result_array.append("".join(stack1_reversed))
        answer = ""
        for each_word in result_array:
            answer += " " + each_word if len(answer) > 0 else each_word
        return answer
```
### A Walktrhough
This Python code defines a `Solution` class with a method `reverseWords` that takes a string `s` as input and returns a new string. This new string is formed by reversing the order of words in `s`, without altering the order of characters within the words themselves. Let's break down how it achieves this:

1. **Initialization**: The method starts by initializing an empty string `word` and an empty list `result_array`. The string `word` will be used to temporarily store characters of the current word being processed, and `result_array` will hold all the words found in the string `s` after they have been processed and reversed.

2. **Reading the Sentence Backwards**: The method iterates over the string `s` from the end to the beginning. This reverse iteration is achieved by the for loop:
   ```python
   for str_index in range(len(s)-1, -1, -1):
   ```
   The `range` function is set up to start from the last index of `s` (`len(s)-1`) and decrement until it reaches `-1` (which stops the iteration), effectively reading `s` backwards.

3. **Word Processing**: During the iteration, the method checks each character. If a space character (`" "`) is encountered, it signifies the end of a word (since we're iterating backwards), and the following steps are taken:
   - If `word` is not empty, it indicates that a complete word has been gathered in reverse order. This word is then reversed again to restore its original order, added to `result_array`, and `word` is reset to an empty string.
   - This double reversal is necessary because we're collecting the characters of the word in reverse as we encounter them.

4. **Handling the Last Word**: Since the last word (which is the first word of the sentence in the original order) won't be followed by a space in the iteration, there's a special condition to handle it when `str_index` reaches `0`. The collected characters in `word` are reversed and added to `result_array` similarly.

5. **Building the Final Answer**: After all words have been processed and stored in `result_array` in reverse order, the method concatenates them into a single string `answer`, separated by spaces. This step constructs the final string with words in reverse order but characters in correct order within each word.

6. **Return Statement**: Finally, the constructed string `answer` is returned as the output of the method.

This method effectively reverses the order of words in a given string without reversing the characters within the words. However, it's important to note that the process involves manually reversing each word twice, which might not be the most efficient way to achieve this result. A more streamlined approach could involve using Python's built-in methods for string and list manipulation, such as splitting the string into words, reversing the list of words, and then joining them back into a string.
