""" Section 08: Sorted Dictionaries and Sets"""

from typing import List
from sortedcontainers import SortedDict, SortedSet


def challenge1():
    def remove_keys(
        sorted_dict: SortedDict[str, int], keys: List[str]
    ) -> SortedDict[str, int]:
        try:
            for key in keys:
                del sorted_dict[key]
        except KeyError as err:
            print("KeyError occured", err)
        return sorted_dict

    def get_values_before_target(
        sorted_dict: SortedDict[str, int], target: str
    ) -> List[int]:
        results = []
        for key, value in sorted_dict.items():
            if key < target:
                results.append(value)
            else:
                break
        return results

    # do not modify below this line
    print(remove_keys(SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35}), ["Bob"]))
    print(
        remove_keys(
            SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}),
            ["Bob", "David"],
        )
    )
    print(
        remove_keys(
            SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40, "Eve": 45}),
            ["Alice", "Eve"],
        )
    )

    print(
        get_values_before_target(
            SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35}), "Bob"
        )
    )
    print(
        get_values_before_target(
            SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}), "David"
        )
    )
    print(
        get_values_before_target(
            SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}), "Charlie"
        )
    )
    print(
        get_values_before_target(
            SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}), "Bob"
        )
    )
    print(
        get_values_before_target(
            SortedDict({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}), "Alice"
        )
    )

    # EXPECTED OUTPUT:
    # SortedDict({'Alice': 25, 'Charlie': 35})
    # SortedDict({'Alice': 25, 'Charlie': 35})
    # SortedDict({'Bob': 30, 'Charlie': 35, 'David': 40})
    # [25]
    # [25, 30, 35]
    # [25, 30]
    # [25]
    # []


def challenge2():
    """pass"""

    def get_first_three(
        sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]
    ) -> List[int]:
        for num in nums1:
            sorted_set.add(num)
        for num in nums2:
            if num in sorted_set:
                sorted_set.remove(num)
        return [sorted_set[idx] for idx in range(3)]

    # do not modify below this line
    print(get_first_three(SortedSet(), [1, 2, 3], [4]))
    print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
    print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
    print(
        get_first_three(
            SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]),
            [10, 11, 12],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        )
    )
    # EXPECTED OUTPUT:
    # [1, 2, 3]
    # [4, 8, 9]
    # [1, 2, 3]
    # [10, 11, 12]


# Testing Grounds:
print("\nChallenge 1: ")
challenge1()

print("\nChallenge 2: ")
challenge2()
