"""importing unittest module to test solutions"""
import unittest


def double_this_list(nums: list) -> list:
    """
        Given an integer array `nums` of length `n`, you want to create
    an array `ans` of length `2n` where `ans[i] == nums[i]` and
    `ans[i + n] == nums[i]` for `0 <= i < n` (0-indexed).

    Specifically, ans is the concatenation of two nums arrays.

    Return the array ans.
    :type nums: List[int]
    :return type: List[int]
    """
    # ======= Start HERE =========


class TestDoubleThisList(unittest.TestCase):
    """ Testing: TODO"""

    def test0(self):
        """ Testing: TODO"""
        assert double_this_list([1, 2, 3]) == [1, 2, 3, 1, 2, 3]

    def test1(self):
        """ Testing: TODO"""
        assert double_this_list([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]

    def test2(self):
        """ Testing: TODO"""
        assert not double_this_list([])

    def test3(self):
        """ Testing: TODO"""
        assert double_this_list([1]) == [1, 1]


if __name__ == "__main__":
    unittest.main()
