# importing unittest in order to test solution.
import unittest


def sum_to_target(my_list: list, target_value: int) -> list:
    """
        :type strs: List[str]
        :rtype: str
    """
    """WRITE YOUR SOLUTION BELOW"""


"""TESTS ARENA:"""


# TEST ARENA
class TestingSumToTarget(unittest.TestCase):
    """PROTO: TODO"""

    def test_none_matching_sub_arr1(self):
        """ input: list, """
        self.assertEqual(sum_to_target(
            my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value=16), [])

    def test_none_matching_sub_arr2(self):
        """PROTO: TODO"""
        self.assertEqual(sum_to_target(
            my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value=13), [])

    def test_found_matching_sub_arr3(self):
        """PROTO: TODO"""
        self.assertEqual(sum_to_target(
            [8, 4, 5, 0, 3, 2, 1, 6, 7, 9], 6), [3, 6], "✅!")

    def test_found_matching_sub_arr4(self):
        """PROTO: TODO"""
        self.assertEqual(sum_to_target(
            [8, 4, 5, 0, 3, 2, 1, 6, 7, 9], 10), [2, 5], "✅!")

    # IF ALL above passed!, activate the ones below:
    # RAINY DAY TESTS:
    # def test_target_arg_is_nonetype(self):
        """PROTO: TODO"""
    #   self.assertEqual(sum_to_target(
    #         my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value=None), "✅!")

    # def test_list_arg_is_nonetype(self):
    #   """PROTO: TODO"""
    #   self.assertEqual(sum_to_target(
    #   my_list=None, target_value=10), [], "✅!")

    # def test_list_arg_is_empty(self):
    #   """PROTO: TODO"""
    #   self.assertEqual(sum_to_target(
    #         my_list=[], target_value=10), [], "✅!")

    # def test_list_arg_is_not_integer(self):
    #   """PROTO: TODO"""
    #     self.assertEqual(sum_to_target(
    #         my_list=[8, 4, 5, 0, 3, 2, 1, 6, 7, 9], target_value="Hello",),  "✅!")


if __name__ == "__main__":
    unittest.main()
