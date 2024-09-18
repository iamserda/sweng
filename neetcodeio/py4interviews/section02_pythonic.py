from typing import List, Tuple, Dict

def challenge1():
    """pass"""

    def sum_3_integers(triplet: List[int]) -> int:
        """pass"""
        int1, int2, int3 = triplet
        return int1 + int2 + int3

    def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
        """pass"""
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
    """pass"""
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


# """Challenge 3
# Implement the following functions using enumerate():

# get_index_of_seven(nums:
# List[int]) -> int that returns the index of the first occurrence of the number 7 in the list nums,
# or -1 if 7 is not found.
# get_dist_between_sevens(nums: List[int]) -> int that returns the distance between the first
# and second occurrence of the number 7 in the list nums.
# You may assume that there will always be at least two occurrences of the number 7 in the list.

# expected output:
# 6
# -1
# 2
# 4
# 1
# 5 """


def challenge3():
    """challenge 3"""

    def get_index_of_seven(nums: List[int]) -> int:
        for start in range(len(nums)):
            if nums[start] == 7:
                return start
        return -1

    def get_dist_between_sevens(nums: List[int]) -> int:
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] == 7:
                if start == -1:
                    start = i
                else:
                    end = i
                    break
        # if start == 0:
        #     return end - start + 1
        return end - start

    # do not modify below this line
    print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
    print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

    print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
    print(get_dist_between_sevens([2, 7, 7, 7, 8]))
    print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))


# using enumerate:
def challenge3a():
    def get_index_of_seven(nums: List[int]) -> int:
        for index, value in enumerate(nums):
            if value == 7:
                return index
        return -1

    def get_dist_between_sevens(nums: List[int]) -> int:
        start = -1
        end = -1
        for index, value in enumerate(nums):
            if value == 7:
                if start == -1:
                    start = index
                else:
                    end = index
                    break
        # if start == 0:
        #     return end - start + 1
        return end - start

    # do not modify below this line
    print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
    print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

    print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
    print(get_dist_between_sevens([2, 7, 7, 7, 8]))
    print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))

def challenge4():
    
    """
    Challenge
    Implement the following function using zip(): 
    group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int] 
    that takes two lists, names and scores, and returns a dictionary 
    where the key is names[i] and it maps to scores[i] as the value.
    """
    

    def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:

        return { key: value for key, value in zip(names, scores)}

    # do not modify below this line
    print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
    print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
    print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
    

#challenge 5:
def challenge5():
    """Challenge
    Implement the following function:
    is_arr_valid(names: List[str], max_length: int) -> bool. 
    It should return True if the length of the names list 
    is greater than 0 and less than or equal to the parameter max_length. 
    Otherwise it should return False."""
    
    def is_arr_valid(names: List[str], max_length: int) -> bool:
        return 0 < len(names) <= max_length

    # do not modify below this line
    print(is_arr_valid(["Alice", "Bob", "Charlie"], 3)) # True
    print(is_arr_valid(["Alice", "Bob", "Charlie"], 2)) # Flase
    print(is_arr_valid(["Alice", "Bob", "Charlie"], 0)) # Flase
    print(is_arr_valid(["Alice", "Bob", "Charlie"], 1)) # Flase
    print(is_arr_valid(["Alice", "Bob", "Charlie"], 4)) # True

# Execute:
# challenge1()
# challenge2()
# challenge3()
# challenge3a()
# challenge4()
challenge5()
# challenge6()
