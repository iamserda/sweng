# Logarithmic Time Complexity Explained (Like You're 10)

## Introduction

Hey there! 👋 Welcome to this simple guide where we're going to talk about something called "Logarithmic Time Complexity." It might sound like a big, fancy phrase, but it's actually a really cool and simple idea once you get to know it. So let's dive in!

## What is Logarithmic Time Complexity?

Imagine you have a huge book, like a Harry Potter book, and you want to find the page where Harry first meets Dobby. You could start from page one and go page by page, but that would take a long time, right?

Instead, you might open the book to the middle, see if you've gone too far or not far enough, and then keep halving the sections like this until you find the page you want. This way of searching is much faster and is what we call "Logarithmic Time Complexity." In computer talk, we often write this as "O(log n)."

## Why is it Important?

Logarithmic time complexity is super important because it helps computers do things quickly. When a computer program can use this kind of "shortcut" (like we did with the Harry Potter book), it means it can work with really big lists of things (like names, numbers, or even Pokémon) super fast without having to look at every single item one by one.

## A Real-World Example

Let's think about a game of "Guess the Number." I'm thinking of a number between 1 and 100, and you have to guess it. Each time you guess, I'll tell you if your guess is too high or too low. If you guess by trying each number one at a time (1, 2, 3, and so on), it could take up to 100 guesses!

But if you start with 50 and I say it's too high, then you try 25 and I say it's too low, and you keep halving the range like this, you'll find the number in just a few guesses. That's the magic of logarithmic time!

## Computer Example

In computers, a famous example of logarithmic time complexity is in something called "Binary Search." It's like our book example. If you have a sorted list of your favorite video games and want to find if "Super Mario" is in there, the computer can start in the middle, eliminate half the list, and keep going like that until it finds the game or realizes it's not there.

## Conclusion

So, that's logarithmic time complexity! It's all about finding faster ways to do things, especially when dealing with lots and lots of items. It's like being a detective who knows the best shortcuts to solving a mystery. 🕵️‍♂️💨

Remember, "Logarithmic Time Complexity" might sound super technical, but it's just a fancy way of saying "finding things quickly by cutting the search area in half each time." Happy exploring! 🌟

## Some Code Examples

Let's provide some code examples to further illustrate logarithmic time complexity, specifically focusing on a common use case: Binary Search. I'll write these examples in Python, which is known for being easy to read and understand.

### Binary Search in a Sorted Array

Binary Search is a classic example of an algorithm with logarithmic time complexity, O(log n). It works on the principle of dividing the search interval in half with each step.

#### Example: Binary Search

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid  # Target found

        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1

        # If target is smaller, ignore right half
        else:
            high = mid - 1

    return -1  # Target not found in the array

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11

result = binary_search(arr, target)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
```

In this example, the `binary_search` function takes a sorted array `arr` and a `target` value. It repeatedly divides the search interval in half. If the value of the search key is less than the item in the middle of the interval, it narrows down the interval to the lower half. Otherwise, it narrows it to the upper half. Repeatedly check until the value is found or the interval is empty.

### Logarithmic Time Complexity in Trees

Another common place we see logarithmic time complexity is in tree structures, especially balanced binary search trees.

#### Example: Searching in a Binary Search Tree

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def search(root, key):
    # Base case: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

# Example usage
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

key = 15
if search(root, key):
    print(f"Element {key} is present in the tree")
else:
    print(f"Element {key} is not present in the tree")
```

In this tree example, each step reduces the problem size by half, either moving left or right based on the comparison, demonstrating logarithmic complexity in a tree structure.

These examples should help in understanding how logarithmic time complexity works in practice with simple and intuitive Python code.

## Author

gh: [@iamserda](https://github.com/iamserda)

tw: [@iamserda](https://twitter.com/iamserda)

in: [@iamserda](https://linkedin.com/in/iamserda)