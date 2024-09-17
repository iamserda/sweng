def challenge1():
    from typing import List, Tuple

    def sum_3_integers(triplet: List[int]) -> int:
        int1, int2, int3 = triplet
        return int1 + int2 + int3

    def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
        w, h, d = box_dimensions
        volume = w * h * d
        return volume

    # do not modify below this line
    print(sum_3_integers([1, 2, 3]))
    print(sum_3_integers([4, 6, 2]))

    print(compute_volume((1, 2, 3)))
    print(compute_volume((3, 2, 1)))
    print(compute_volume((3, 9, 7)))


# Execute:
challenge1()