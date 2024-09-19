"""pass """
from typing import List, Dict

# challenge 1:
def challenge1():
    """pass """
    def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
        """pass """
        return dict( zip(keys, values))

    def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
        """pass """
        return [hash_map[key] for key in keys]


    # do not modify below this line
    print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
    print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
    print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

    print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
    print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
    print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))

    # EXPECTED OUTPUT
    {'Alice': 90, 'Bob': 80, 'Charlie': 70}
    {'Jane': 25, 'Carol': 100, 'Charlie': 60}
    {'Doug': 80, 'Bob': 90, 'Tommy': 100}
    [90, 80, 70]
    [25, 100]
    [78]



# challenge 2:
# challenge 3:
# challenge 4:
# challenge 5:
# challenge 6:
# challenge 7:
# challenge 8:

# TESTING GROUNDS:

challenge1()
# challenge2()
# challenge3()
# challenge4()
# challenge5()
# challenge6()
# challenge7()
# challenge8()