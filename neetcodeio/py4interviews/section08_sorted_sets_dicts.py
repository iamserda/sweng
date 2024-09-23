""" Section 08: Sorted Dictionaries and Sets"""

from typing import List
from sortedcontainers import SortedDict


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
    pass


# Testing Grounds:
challenge1()
challenge2()
