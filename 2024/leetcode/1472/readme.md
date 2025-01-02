# [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/description)


**Difficulty:** Medium

**Topics:**Design, Stack, Array, Linked List

## Companies

This problem may appear in technical interviews at companies that are interested in testing candidates' abilities to design systems or manage state effectively, such as companies working on web browsers, applications with undo-redo functionality, or any software that navigates through a history of states (e.g., Adobe, Google, Microsoft).

## Description

You have a browser of one tab where you start on the `homepage` and you can visit another `url`, get back in the history number of `steps` or move forward in the history number of `steps`.

Implement the `BrowserHistory` class:

- `BrowserHistory(string homepage)` Initializes the object with the `homepage` of the browser.
- `void visit(string url)` Visits `url` from the current page. It clears up all the forward history.
- `string back(int steps)` Move `steps` back in history. If you can only return `x` steps in the history and `steps > x`, you will return only `x` steps. Return the current `url` after moving back in history **at most** `steps`.
- `string forward(int steps)` Move `steps` forward in history. If you can only forward `x` steps in the history and `steps > x`, you will forward only `x` steps. Return the current `url` after moving forward in history **at most** `steps`.

### Examples

**Example 1:**

```plaintext
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[1],[1],[1]]

Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" and return it
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" and return it
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" and return it
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(1);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(1);                   // You are in "linkedin.com", move back to "google.com" and return it
browserHistory.back(1);                   // You are in "google.com", move back to "leetcode.com" and return it
```

### Constraints

- `1 <= homepage.length, url.length <= 20`
- `1 <= steps <= 100`
- `homepage` and `url` consist of '.' or lowercase English letters.
- At most `5000` calls will be made to `visit`, `back`, and `forward`.

## Approach

To implement the `BrowserHistory` class, you can use a combination of two stacks to manage back and forward operations, a doubly linked list where each node contains a URL and pointers to the previous and next URLs, or an array to store the history of URLs along with an index pointer to keep track of the current URL.

Each method's implementation would manipulate these data structures accordingly to simulate the behavior of a browser's history functionality, taking care to handle edge cases such as attempting to move back or forward more steps than the history allows.

The choice of data structure (stack, doubly linked list, array) depends on the desired trade-offs between ease of implementation, memory usage, and operation complexities.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/design-browser-history/description)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
