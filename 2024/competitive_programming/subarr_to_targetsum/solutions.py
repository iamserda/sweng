"""Global imports"""
import unittest


def subarr_sum_to_target_val(my_list: list, target_value: int) -> list:
    """ 
    function takes two args: a list and a target_sum
    Find a contiguous subarr where the values adds up to a target sum.
    If found, return a list containing the start and end indices: [star, end]
    if not found, return None or an empty list: []
    # [8, 4, 5, 0, 3, 2, 1, 6, 7, 9], 10 -> [2, 5]
    """
    if not isinstance(my_list, list):
        raise TypeError(
            f"Expected a 'List', received {type(my_list)}")
    if not my_list:
        raise ValueError("List is empty.")
    if not isinstance(target_value, int):
        raise TypeError(
            f"Expected an 'Integer', received {type(target_value)}")

    list_length = len(my_list)
    start = 0
    end = 0
    sum = 0

    while start < list_length and end < list_length:

        sum += my_list[end]
        if target_value == sum:
            # if the values we have accumulated, adds up to target value
            # we would return start and end end index range.
            return [start, end]

        if sum > target_value:
            # if the current sum is more than our target value,
            # we MUST to move the start index forward by 1.
            # However, before we do so, we must disount
            # the value at index "start" from our sum
            sum -= my_list[start]
            start += 1
        end += 1
        if end >= list_length:
            return []


# TEST ARENA
class TestingSubArraySumToTargetVal(unittest.TestCase):
    def test_none_matching_subarr1(self):
        """ input: list, """
        self.assertEqual(subarr_sum_to_target_val(
            my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value=16), [])

    def test_none_matching_subarr2(self):
        self.assertEqual(subarr_sum_to_target_val(
            my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value=13), [])

    def test_found_matching_sub_arr1(self):
        self.assertEqual(subarr_sum_to_target_val(
            [8, 4, 5, 0, 3, 2, 1, 6, 7, 9], 6), [3, 6], "✅!")

    def test_found_matching_sub_arr2(self):
        self.assertEqual(subarr_sum_to_target_val(
            [8, 4, 5, 0, 3, 2, 1, 6, 7, 9], 10), [2, 5], "✅!")

    # IF ALL above passed!, activate the ones below:
    # RAINY DAY TESTS:
    # def test_target_arg_is_nonetype(self):
    #     self.assertEqual(subarr_sum_to_target_val(
    #         my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value=None), "✅!")

    # def test_list_arg_is_nonetype(self):
    #     self.assertEqual(subarr_sum_to_target_val(
    #         my_list=None, target_value=10), [], "✅!")

    # def test_list_arg_is_empty(self):
    #     self.assertEqual(subarr_sum_to_target_val(
    #         my_list=[], target_value=10), [], "✅!")

    # def test_list_arg_isnot_integer(self):
    #     self.assertEqual(subarr_sum_to_target_val(
    #         my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value="Hello",),  "✅!")


if __name__ == "__main__":
    unittest.main()
