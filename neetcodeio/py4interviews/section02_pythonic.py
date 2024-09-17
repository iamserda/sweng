from typing import List, Tuple

def challenge1():
    """ pass"""

    def sum_3_integers(triplet: List[int]) -> int:
        """ pass"""
        int1, int2, int3 = triplet
        return int1 + int2 + int3

    def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
        """ pass"""
        w, h, d = box_dimensions
        volume = w * h * d
        return volume

    # do not modify below this line
    print(sum_3_integers([1, 2, 3]))
    print(sum_3_integers([4, 6, 2]))

    print(compute_volume((1, 2, 3)))
    print(compute_volume((3, 2, 1)))
    print(compute_volume((3, 9, 7)))


"""
Challenge 2:

Implement the following function using unpacking:

best_student(scores: List[Tuple[str, int]]) -> str: that takes a list of tuples. Each tuple represents the (name, score) of a student. Find the student with the highest score and return their name.
You may assume that a score will never be less than 0 and that only one student will have the highest score.
expected output:
Alice
Charlie
Bob
David"""

def challenge2():
    """ pass"""
    from typing import List, Tuple

    def best_student(scores: List[Tuple[str, int]]) -> str:
        max_score = float("-inf")
        max_name = ""
        for name, score in scores:
            if score > max_score:
                max_score = score
                max_name = name
        return max_name

    # do not modify below this line
    print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
    print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
    print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
    print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))


# Execute:
challenge1()
challenge2()
# challenge3()
# challenge4()
