"""pass """

from typing import List, Dict, Tuple, Counter as CounterType
from collections import defaultdict


# challenge 1:
def challenge1():
    """pass"""

    def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
        """pass"""
        return dict(zip(keys, values))

    def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
        """pass"""
        return [hash_map[key] for key in keys]

    # do not modify below this line
    print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
    print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
    print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

    print(
        get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"])
    )
    print(
        get_values(
            {
                "Jane": 25,
                "Charlie": 60,
                "Carol": 100,
            },
            ["Jane", "Carol"],
        )
    )
    print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))

    # EXPECTED OUTPUT
    # {'Alice': 90, 'Bob': 80, 'Charlie': 70}
    # {'Jane': 25, 'Carol': 100, 'Charlie': 60}
    # {'Doug': 80, 'Bob': 90, 'Tommy': 100}
    # [90, 80, 70]
    # [25, 100]
    # [78]


# challenge 2:
def challenge2():
    """pass"""

    def count_chars(s: str) -> Dict[str, int]:
        my_dictio = {}
        for char in s:
            if char in my_dictio:
                my_dictio[char] += 1
            else:
                my_dictio[char] = 1
        return my_dictio

    def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
        results = {}
        for row in nums:
            results[row[0]] = []
            for idx in range(1, len(row)):
                results[row[0]].append(row[idx])
        return results

    # do not modify below this line
    print(count_chars("hello"))
    print(count_chars("helloworld"))
    print(count_chars("areallylongstringwhyareyoureadingthishahalol"))
    print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
    print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
    print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
    print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
    # EXPECTED OUTPUT:
    # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    # {'a': 6, 'r': 4, 'e': 3, 'l': 5, 'y': 3, 'o': 3, 'n': 3, 'g': 3, 's': 2, 't': 2, 'i': 3, 'w': 1, 'h': 4, 'u': 1, 'd': 1}
    # {1: [4], 4: [5, 6]}
    # {1: [4, 5, 6], 4: [5, 6, 7]}
    # {5: [6, 7, 8, 9], 4: [5, 6, 7, 8]}
    # {3: [2, 3, 4, 5], 4: [5, 6, 7, 8], 5: [6, 7, 8]}


# challenge2a:
def challenge2A():
    """pass"""

    def count_chars(s: str) -> Dict[str, int]:
        dictio = defaultdict(int)
        for char in s:
            dictio[char] += 1
        return dictio

    def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
        results = defaultdict(list)
        for row in nums:
            results[row[0]] += row[1:]
        return results

    # do not modify below this line
    print(count_chars("hello"))
    print(count_chars("helloworld"))
    print(count_chars("areallylongstringwhyareyoureadingthishahalol"))
    print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
    print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
    print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
    print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))

    # EXPECTED OUTPUT:
    # defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})
    # defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})
    # defaultdict(<class 'int'>, {'a': 6, 'r': 4, 'e': 3, 'l': 5, 'y': 3, 'o': 3, 'n': 3, 'g': 3, 's': 2, 't': 2, 'i': 3, 'w': 1, 'h': 4, 'u': 1, 'd': 1})
    # defaultdict(<class 'list'>, {1: [2, 3, 4], 4: [5, 6]})
    # defaultdict(<class 'list'>, {1: [2, 3, 4, 4, 5, 6], 4: [5, 6, 7]})
    # defaultdict(<class 'list'>, {5: [2, 3, 4, 5, 6, 7, 8, 9], 4: [5, 6, 7, 8]})
    # defaultdict(<class 'list'>, {3: [2, 3, 4, 5], 4: [5, 6, 7, 8], 5: [6, 7, 8]})


# challenge 3:
def challenge3():
    from collections import Counter

    def count_chars(s1: str, s2: str) -> CounterType:
        counter = Counter(s1)
        counter.update(s2)
        return counter

    def helper(my_str, my_dictio):
        for char in my_str:
            if char in my_dictio:
                my_dictio[char] += 1
            else:
                my_dictio[char] = 1

    def count_chars_prime(s1: str, s2: str) -> CounterType:
        dictio = {}
        helper(s1, dictio)
        helper(s2, dictio)
        return dictio

    # do not modify below this line
    print(count_chars("hello", "world"))
    print(count_chars("hello", "worldhello"))
    print(count_chars("areallylongstring", "heyhowisitgoing"))

    # do not modify below this line
    print(count_chars_prime("hello", "world"))
    print(count_chars_prime("hello", "worldhello"))
    print(count_chars_prime("areallylongstring", "heyhowisitgoing"))


# challenge 4:
def challenge4():

    def num_to_index(nums: List[int]) -> Dict[int, int]:
        return {value: index for index, value in enumerate(nums)}

    # do not modify below this line
    print(num_to_index([1, 2, 3, 4, 5, 6, 7, 8]))
    print(num_to_index([8, 7, 6, 5, 4, 3, 2, 1]))
    print(num_to_index([0, 3, 2, 4, 5, 1]))

    # Expected Output:
    # {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7}
    # {8: 0, 7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}
    # {0: 0, 3: 1, 2: 2, 4: 3, 5: 4, 1: 5}


# challenge 5:
def challenge5():
    """pass """
    def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
        return list(age_dict.items())

    # do not modify below this line
    print(get_dict_items({"Alice": 25, "Bob": 30, "Charlie": 35}))
    print(get_dict_items({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
    print(
        get_dict_items({"Bob": 30, "David": 40, "Charlie": 35, "Alice": 25, "Eve": 45})
    )
    print(
        get_dict_items(
            {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40, "Eve": 45, "Frank": 50}
        )
    )

def challenge5A():
    """pass """
    def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
        return [ tup for tup in age_dict.items()]
        # do not modify below this line
    print(get_dict_items({"Alice": 25, "Bob": 30, "Charlie": 35}))
    print(get_dict_items({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
    print(
        get_dict_items({"Bob": 30, "David": 40, "Charlie": 35, "Alice": 25, "Eve": 45})
    )
    print(
        get_dict_items(
            {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40, "Eve": 45, "Frank": 50}
        )
    )

    # Expected Output:
    # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
    # [('Alice', 25), ('Bob', 30), ('Charlie', 35), ('David', 40)]
    # [('Bob', 30), ('David', 40), ('Charlie', 35), ('Alice', 25), ('Eve', 45)]
    # [('Alice', 25), ('Bob', 30), ('Charlie', 35), ('David', 40), ('Eve', 45), ('Frank', 50)]


# challenge 6:
def challenge6():
    pass


# challenge 7:
def challenge7():
    pass


# challenge 8:
def challenge8():
    pass


# TESTING GROUNDS:
print("\nChallenge 1: ")
challenge1()
print("\nChallenge 2: ")
challenge2()
print("\nChallenge 2A: ")
challenge2A()
print("\nChallenge 3: ")
challenge3()
print("\nChallenge 4: ")
challenge4()
print("\nChallenge 5: ")
challenge5()
print("\nChallenge 5A: ")
challenge5A()
print("\nChallenge 6: ")
challenge6()
print("\nChallenge 7: ")
challenge7()
print("\nChallenge 8: ")
challenge8()
