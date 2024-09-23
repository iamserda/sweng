from typing import List


def challenge1():
    def sort_words(words: List[str]) -> List[str]:
        words.sort()
        return words

    def sort_numbers(numbers: List[int]) -> List[int]:
        numbers.sort()
        return numbers

    def sort_decimals(numbers: List[float]) -> List[float]:
        numbers.sort()
        return numbers

    # do not modify below this line
    # expected_output: # ['apple', 'banana', 'blueberry', 'cherry', 'kiwi', 'pear', 'watermelon', 'zucchini']
    print(
        "\n",
        sort_words(
            [
                "cherry",
                "apple",
                "blueberry",
                "banana",
                "watermelon",
                "zucchini",
                "kiwi",
                "pear",
            ]
        ),
    )

    # expected_output: [1, 2, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 9, 11, 19]
    print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

    # expected_output: [2.82, 3.14, 6.433, 7.9, 21.554, 21.555]
    print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))


def challenge2():
    def reverse_sort_words(words: List[str]) -> List[str]:
        words.sort(reverse=True)
        return words

    def reverse_sort_numbers(numbers: List[int]) -> List[int]:
        numbers.sort(reverse=True)
        return numbers

    def reverse_sort_decimals(numbers: List[float]) -> List[float]:
        numbers.sort(reverse=True)
        return numbers

    # do not modify below this line
    print(
        "\n",
        reverse_sort_words(
            [
                "cherry",
                "apple",
                "blueberry",
                "banana",
                "watermelon",
                "zucchini",
                "kiwi",
                "pear",
            ]
        ),
    )

    print(reverse_sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

    print(reverse_sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))


def challenge3():
    # CHALLENGE 3:
    """
    Challenge
    Implement the following functions:

    sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns a new list of words sorted based on their length, in descending order.
    sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns a new list of numbers sorted based on their absolute value, in ascending order. Hint: You may use the abs() function to get the absolute value of a number.
    Hint: You may define additional functions. Functions defined in the global scope are accessible within other functions.
    """

    def sort_wordsC(words: List[str]) -> List[str]:
        words.sort(key=lambda a: len(a), reverse=True)
        return words

    def sort_numbersC(numbers: List[int]) -> List[int]:
        numbers.sort(key=abs)
        return numbers

    # do not modify below this line
    print(
        "\n",
        sort_wordsC(
            [
                "cherry",
                "apple",
                "blueberry",
                "banana",
                "watermelon",
                "zucchini",
                "kiwi",
                "pear",
            ]
        ),
    )

    print(sort_numbersC([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))


# challenge 4
def challenge4():
    """
    Challenge
    Implement the following functions:
    sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns a new list of words sorted in ascending order. Do not modify the original list.
    sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns a new list of numbers sorted in descending order based on their absolute value. Do not modify the original list.

    expected output:
    ['cherry', 'apple', 'blueberry', 'banana', 'watermelon', 'zucchini', 'kiwi', 'pear']
    ['apple', 'banana', 'blueberry', 'cherry', 'kiwi', 'pear', 'watermelon', 'zucchini']
    [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]
    [-19, 11, 9, 7, -6, 6, -5, 5, 4, -4, -3, 2, -2, 2, 1]

    """

    def sort_wordsD(words: List[str]) -> List[str]:
        return sorted(words)

    def sort_numbersD(numbers: List[int]) -> List[int]:
        return sorted(numbers, key=abs, reverse=True)

    # do not modify below this line
    print()
    original_words = [
        "cherry",
        "apple",
        "blueberry",
        "banana",
        "watermelon",
        "zucchini",
        "kiwi",
        "pear",
    ]
    original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

    print(original_words)
    print(sort_wordsD(original_words))
    print(original_numbers)
    print(sort_numbersD(original_numbers))


# TESTING GROUND:
print("\nChallenge 1: ")
challenge1()
print("\nChallenge 2: ")
challenge2()
print("\nChallenge 3: ")
challenge3()
print("\nChallenge 4: ")
challenge4()
