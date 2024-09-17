from typing import List


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
#expected_output: # ['apple', 'banana', 'blueberry', 'cherry', 'kiwi', 'pear', 'watermelon', 'zucchini']
print("\n",sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

# expected_output: [1, 2, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 9, 11, 19]
print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

# expected_output: [2.82, 3.14, 6.433, 7.9, 21.554, 21.555]
print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))




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
print("\n",reverse_sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(reverse_sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(reverse_sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
