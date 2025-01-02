import unittest


"""WRITE YOUR SOLUTION BELOW"""


def longest_common_prefix(string_list: list[str]) -> str:
    """
        :type strs: List[str]
        :rtype: str
        """


"""TESTS ARENA:"""


class TestLongestCommonPrefix(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(longest_common_prefix(
            ["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_empty_list(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_single_string(self):
        self.assertEqual(longest_common_prefix(["alone"]), "alone")

    def test_no_common_prefix(self):
        self.assertEqual(longest_common_prefix(["abc", "def", "ghi"]), "")

    def test_varied_length_strings(self):
        self.assertEqual(longest_common_prefix(["a", "ab", "abc"]), "a")
        self.assertEqual(longest_common_prefix(
            ["longest", "longer", "long"]), "long")


if __name__ == "__main__":
    unittest.main()
